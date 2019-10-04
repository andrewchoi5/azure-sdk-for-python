# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_py3 import Resource


class BillingProfile(Resource):
    """A billing profile resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param display_name: The billing profile name.
    :type display_name: str
    :param po_number: Purchase order number.
    :type po_number: str
    :param address: Billing address.
    :type address: ~azure.mgmt.billing.models.AddressDetails
    :param invoice_email_opt_in: If the billing profile is opted in to receive
     invoices via email.
    :type invoice_email_opt_in: bool
    :ivar invoice_day: Invoice day.
    :vartype invoice_day: int
    :ivar currency: The currency associated with the billing profile.
    :vartype currency: str
    :param enabled_azure_plans: Information about the enabled azure plans.
    :type enabled_azure_plans: list[~azure.mgmt.billing.models.AzurePlan]
    :param invoice_sections: The invoice sections associated to the billing
     profile.
    :type invoice_sections: list[~azure.mgmt.billing.models.InvoiceSection]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'invoice_day': {'readonly': True},
        'currency': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'po_number': {'key': 'properties.poNumber', 'type': 'str'},
        'address': {'key': 'properties.address', 'type': 'AddressDetails'},
        'invoice_email_opt_in': {'key': 'properties.invoiceEmailOptIn', 'type': 'bool'},
        'invoice_day': {'key': 'properties.invoiceDay', 'type': 'int'},
        'currency': {'key': 'properties.currency', 'type': 'str'},
        'enabled_azure_plans': {'key': 'properties.enabledAzurePlans', 'type': '[AzurePlan]'},
        'invoice_sections': {'key': 'properties.invoiceSections', 'type': '[InvoiceSection]'},
    }

    def __init__(self, *, display_name: str=None, po_number: str=None, address=None, invoice_email_opt_in: bool=None, enabled_azure_plans=None, invoice_sections=None, **kwargs) -> None:
        super(BillingProfile, self).__init__(**kwargs)
        self.display_name = display_name
        self.po_number = po_number
        self.address = address
        self.invoice_email_opt_in = invoice_email_opt_in
        self.invoice_day = None
        self.currency = None
        self.enabled_azure_plans = enabled_azure_plans
        self.invoice_sections = invoice_sections
