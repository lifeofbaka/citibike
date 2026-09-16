import dagster as dg 


@dg.asset
def citibike_pipeline_definition():
    """
    This function defines the Citibike pipeline using Dagster.
    It can be expanded to include more complex logic and dependencies.
    """
    return "Citibike pipeline definition"
    
# only opjects in the difinitions will be used in the pipeline orchestration.
defs = dg.Definitions(
    assets=[citibike_pipeline_definition],
    resources={},
    schedules=[],
    sensors=[],
)