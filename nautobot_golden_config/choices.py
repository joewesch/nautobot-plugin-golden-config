"""Choicesets for golden config."""
from nautobot.utilities.choices import ChoiceSet


class ComplianceRuleTypeChoice(ChoiceSet):
    """Choiceset used by ComplianceRule."""

    TYPE_CLI = "cli"
    TYPE_JSON = "json"
    TYPE_CUSTOM = "custom"

    CHOICES = (
        (TYPE_CLI, "CLI"),
        (TYPE_JSON, "JSON"),
        (TYPE_CUSTOM, "CUSTOM"),
    )


class ConfigPlanTypeChoice(ChoiceSet):
    """Choiceset used by ConfigPlan."""

    TYPE_INTENDED = "intended"
    TYPE_MISSING = "missing"
    TYPE_REMEDIATION = "remediation"
    TYPE_MANUAL = "manual"
    TYPE_FULL = "full"

    CHOICES = (
        (TYPE_INTENDED, "Intended"),
        (TYPE_MISSING, "Missing"),
        (TYPE_REMEDIATION, "Remediation"),
        (TYPE_MANUAL, "Manual"),
        (TYPE_FULL, "Full"),
    )
