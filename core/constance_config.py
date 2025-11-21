import json
from django.utils.translation import gettext_lazy as _
from unfold.contrib.constance.settings import UNFOLD_CONSTANCE_ADDITIONAL_FIELDS

CONSTANCE_ADDITIONAL_FIELDS = {
    **UNFOLD_CONSTANCE_ADDITIONAL_FIELDS,

    bool: [
        "django.forms.BooleanField",
        {
            "widget": "unfold.widgets.UnfoldBooleanSwitchWidget",
            "required": False,
        },
    ],

    "announcing": [
        "django.forms.CharField",
        {
            "widget": "unfold.widgets.UnfoldAdminTextareaWidget",
        },
    ],
}

DEFAULT_ANNOUNCING = [
    {
        "en": "",
        "fr": ""
    }
]

FANTASY_CRAFT_LATEST = "0.01"

# Define the config keys, their default values, and help text
CONSTANCE_CONFIG = {
    "ANNOUNCING": (json.dumps(DEFAULT_ANNOUNCING), _("Announcements displayed on the homepage"), "announcing"),
    "FANTASY_CRAFT_LATEST": (FANTASY_CRAFT_LATEST, _("Latest version of Fantasy Craft"))
}
