from typing import List
from google.cloud import datacatalog_v1


class DataCatalogService():
    """Data Catalog Service"""

    def __init__(self):
        self.client = datacatalog_v1.DataCatalogClient()
        self.scope = datacatalog_v1.types.SearchCatalogRequest.Scope()

    def search_catalog_in_projects(
        self,
        project_ids: List[str],
        query: str
    ):
        for project_id in project_ids:
            self.scope.include_project_ids.append(project_id)

        return self.client.search_catalog(
            scope=self.scope,
            query=query
        )

    def search_catalog_in_organisations(
        self,
        organisation_ids: List[str],
        query: str
    ):
        for organisation_id in organisation_ids:
            self.scope.include_org_ids.append(organisation_id)

        return self.client.search_catalog(
            scope=self.scope,
            query=query
        )

    def lookup_entry_linked_resource(
        self,
        linked_resource: str
    ):
        request = datacatalog_v1.LookupEntryRequest(
            linked_resource=linked_resource,
        )

        return self.client.lookup_entry(
            request=request
        )

    def lookup_entry_sql_resource(
        self,
        sql_resource: str
    ):
        request = datacatalog_v1.LookupEntryRequest(
            sql_resource=sql_resource,
        )

        return self.client.lookup_entry(
            request=request
        )

    def lookup_entry_fully_qualified_name(
        self,
        fully_qualified_name: str
    ):
        request = datacatalog_v1.LookupEntryRequest(
            fully_qualified_name=fully_qualified_name,
        )

        return self.client.lookup_entry(
            request=request
        )
