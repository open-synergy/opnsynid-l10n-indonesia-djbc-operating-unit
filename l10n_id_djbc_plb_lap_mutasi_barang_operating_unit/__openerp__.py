# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Indonesia - Lap. Mutasi Barang for DJBC's "
    "Pusat Logistik Berikat Operating Unit",
    "version": "8.0.1.0.0",
    "category": "localization",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "l10n_id_djbc_plb_lap_mutasi_barang",
        "product_operating_unit",
        "stock_operating_unit",
    ],
    "data": [
        "security/plb_lap_mutasi_barang_security.xml",
    ],
}
