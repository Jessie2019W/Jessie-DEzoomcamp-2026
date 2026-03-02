"""marimo notebook to explore the NYC taxi dataset loaded by `taxi_pipeline`.

Run with:
    marimo edit taxi_explore_marimo.py
"""

import marimo

__generated_with = "0.20.2"
app = marimo.App()


@app.cell
def _():
    import dlt
    import ibis
    import altair as alt

    return dlt, ibis


@app.cell
def _(dlt):
    pipeline = dlt.attach("taxi_pipeline")
    dataset = pipeline.dataset()
    # Get ibis connection for rich data exploration
    ibis_con = dataset.ibis()
    dataset_name = pipeline.dataset_name

    print(dataset_name)
    return dataset_name, ibis_con


@app.cell
def _(dataset_name, ibis, ibis_con):
    # Table name corresponds to the dlt resource defined in `taxi_pipeline.py`.
    table = ibis_con.table("nyc_taxi_trips", database=dataset_name)
    taxi_query = (
            table
            .order_by(ibis.desc("trip_dropoff_date_time"))
            .limit(20)
        )
    taxi_df = taxi_query.to_pandas()
    print(taxi_df)
    return (table,)


@app.cell
def _(table):
    # Date range of the dataset based on pickup datetime.
    date_range_expr = table.aggregate(
        min_pickup=table.trip_pickup_date_time.min(),
        max_dropoff=table.trip_dropoff_date_time.max(),
    )
    date_range = date_range_expr.to_pandas()
    date_range
    return


@app.cell
def _(table):
    # Proportion of trips for each payment type.
    trips_by_payment_expr = table.group_by("payment_type").aggregate(
        trip_count=table.payment_type.count(),
    )
    trips_by_payment = trips_by_payment_expr.to_pandas()
    total_trips = trips_by_payment["trip_count"].sum()
    trips_by_payment["proportion"] = (
        trips_by_payment["trip_count"] / total_trips
    ).map("{:.2%}".format)

    trips_by_payment
    return


@app.cell
def _(table):
    # Total amount of money generated in tips.
    total_tips_expr = table.aggregate(total_tip_amount=table.tip_amt.sum())
    total_tips = total_tips_expr.to_pandas()
    total_tips
    return


if __name__ == "__main__":
    app.run()
