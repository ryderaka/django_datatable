# Created by thoughtchimp on 28/02/18
# -*- coding: utf-8 -*-

from table import Table
from table.columns import Column
from datatable.models import EmbedError


class EmbedErrorTable(Table):
    id = Column(field='id', header='#')
    # compress_url = Column(field='compress_url', header='Compress Url')
    url = Column(field='url', header='Url')
    error = Column(field='error', header='Error')
    status_code = Column(field='status_code', header='Status Code')
    timestamp = Column(field='timestamp', header='Timestamp')

    class Meta:
        model = EmbedError
