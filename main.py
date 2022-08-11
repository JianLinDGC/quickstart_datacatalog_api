from app.services.data_catalog_api import DataCatalogService
from config import PROJECT_IDS, ORGANISATION_IDS


def main():
    data_catalog_service = DataCatalogService()

    search_catalog_projects_example(data_catalog_service)
    search_catalog_organisations_example(data_catalog_service)

    lookup_entry_linked_resource_example(data_catalog_service)
    lookup_entry_sql_resource_example(data_catalog_service)
    lookup_entry_fully_qualified_name_example(data_catalog_service)


def search_catalog_projects_example(data_catalog_service):
    # Add a query, for example search catalog with a label named created_by: label=created_by
    query = ''

    search_results = data_catalog_service.search_catalog_in_projects(
        PROJECT_IDS,
        query
    )

    results_list = [result for result in search_results]
    for result in results_list:
        print(result)

    print(f"Number of results: {len(results_list)}")


def search_catalog_organisations_example(data_catalog_service):
    # Add a query, for example search catalog with a label named created_by: label=created_by
    query = ''

    search_results = data_catalog_service.search_catalog_in_organisations(
        ORGANISATION_IDS,
        query
    )

    results_list = [result for result in search_results]
    for result in results_list:
        print(result)

    print(f"Number of results: {len(results_list)}")


def lookup_entry_linked_resource_example(data_catalog_service):
    # Full name of GCP resource
    # Example: //bigquery.googleapis.com/projects/{PROJECT_ID}/datasets/{DATASET_ID}/tables/{TABLE_ID}
    linked_resource = ''

    entry = data_catalog_service.lookup_entry_linked_resource(
        linked_resource = linked_resource
    )

    print(entry)


def lookup_entry_sql_resource_example(data_catalog_service):
    # SQL name of entry (case sensitive)
    # Example: bigquery.table.`{PROJECT_ID}`.`{DATASET_ID}`.`{TABLE_ID}`
    sql_resource = ''

    entry = data_catalog_service.lookup_entry_sql_resource(
        sql_resource=sql_resource
    )

    print(entry)


def lookup_entry_fully_qualified_name_example(data_catalog_service):
    # Fully qualified name of resource
    # Example: {SYSTEM}:{PROJECT}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}
    fqn_resource = ''

    entry = data_catalog_service.lookup_entry_fully_qualified_name(
        fully_qualified_name=fqn_resource
    )

    print(entry)


if __name__ == '__main__':
    main()
