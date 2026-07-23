"""Regression tests for ``clone_seed.substitute`` — the Clone Agent's name
substitution.

The skill-prefix rule (``al_ -> ac_``, built from the package initials in
``PyAutoBrain/agents/conductors/clone/_clone.py``) exists to rename skill files
at birth: ``al_fit_model.md -> ac_fit_model.md``. As a bare ``str.replace`` it
also rewrote the ``al_`` *inside* ordinary identifiers, which is how a sibling
assistant clone was born with ``totac_draws``, ``externac_shear.yaml`` and
``radiac_minimum`` (PyAutoBrain#150). Two of those were live config keys that
silently stopped overriding; five were prior files that could no longer be found
for their classes.

The rule must still apply to file *text*, because skills cross-reference each
other by name in prose — a path-only rule would leave broken links in every
newborn. So it is word-anchored instead: it may start a token, never continue
one.
"""

import pytest

from autohands.clone_seed import substitute

# Fixture names are deliberately fictional, not live satellite repos: this file
# is organ code under the tenant firewall, and a fork must not inherit a test
# asserting on repos it does not have. The ``al_ -> ac_`` prefix pair is the one
# thing that must stay literal — the corrupted identifiers below (``total_draws``,
# ``external_shear``, ``radial_minimum``) only demonstrate the mid-token bug
# because they contain ``al_``.
SKILL_PREFIX = ("al_", "ac_", "word")
FULL_NAME = ("alpha_assistant", "beta_assistant")
PACKAGE = ("autoalpha", "autobeta")
LIBRARY = ("PyAutoAlpha", "PyAutoBeta")


@pytest.mark.parametrize(
    "text, expected",
    [
        ("al_fit_model.md", "ac_fit_model.md"),           # start of string
        ("skills/al_fit_model.md", "skills/ac_fit_model.md"),  # after a path separator
        ("see `al_audit` for details", "see `ac_audit` for details"),  # after a backtick
        ("run al_audit now", "run ac_audit now"),         # after a space
        ("(al_audit)", "(ac_audit)"),                     # after a bracket
    ],
)
def test_word_anchored_rule_renames_at_a_token_boundary(text, expected):
    assert substitute(text, [SKILL_PREFIX]) == expected


@pytest.mark.parametrize(
    "text",
    [
        "total_draws",        # a live sampler param — was corrupted to totac_draws
        "total_contours",     # a live plot config key — was corrupted to totac_contours
        "external_shear",     # was corrupted to externac_shear
        "isothermal_core",    # was corrupted to isothermac_core
        "exponential_core",   # was corrupted to exponentiac_core
        "virial_mass_conc",   # was corrupted to viriac_mass_conc
        "radial_minimum",     # was corrupted to radiac_minimum
        "  total_draws: 50",  # as it appears in a yaml body
        "config/priors/mass/sheets/external_shear.yaml",  # as it appears in a path
    ],
)
def test_word_anchored_rule_never_matches_mid_token(text):
    assert substitute(text, [SKILL_PREFIX]) == text


def test_two_element_rules_keep_plain_replace_semantics():
    """Existing plan JSON has no third element — those rules must be unchanged,
    including where they legitimately match inside a longer token."""
    assert substitute("autoalpha_workspace", [PACKAGE]) == "autobeta_workspace"
    assert substitute("PyAutoAlpha", [LIBRARY]) == "PyAutoBeta"


def test_full_substitution_list_on_a_realistic_body():
    """The four rules in _clone.py order, over text containing both a skill
    reference (must rename) and ordinary identifiers (must not)."""
    subs = [FULL_NAME, SKILL_PREFIX, LIBRARY, PACKAGE]
    body = (
        "# alpha_assistant\n"
        "See `al_fit_model.md`. Built on PyAutoAlpha (autoalpha).\n"
        "total_draws: 50\n"
        "external_shear: 0.05\n"
    )
    assert substitute(body, subs) == (
        "# beta_assistant\n"
        "See `ac_fit_model.md`. Built on PyAutoBeta (autobeta).\n"
        "total_draws: 50\n"
        "external_shear: 0.05\n"
    )
