def map_sql_row_to_result(row, columns):
    properties = []
    for col, val in zip(columns, row):
        if col == "titolo":
            properties.append({"property_name": "name", "property_value": val})
        else:
            properties.append({"property_name": col, "property_value": val})
    return {
        "item_type": "film",
        "properties": properties
    }
