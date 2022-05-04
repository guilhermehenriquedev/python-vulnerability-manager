from django.db import models
from django.utils.translation import gettext as _


class AssetVulnerability(models.Model):
    ID = models.AutoField(_("id"), primary_key=True)
    ASSET_HOSTNAME = models.CharField(_("hostname"), max_length=255)
    ASSET_IP_ADDRESS = models.CharField(_("ip_address"), max_length=255)
    VULNERABILITY_TITLE = models.CharField(_("title"), max_length=255)
    VULNERABILITY_SEVERITY = models.CharField(_("severity"), max_length=255)
    VULNERABILITY_CVSS = models.DecimalField(_("cvss"), max_digits=15, decimal_places=2)
    VULNERABILITY_PUBLICATION_DATE = models.DateField(_("publication_date"), blank=True, null=True)

