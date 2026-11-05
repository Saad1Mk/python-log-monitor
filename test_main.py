import pytest 
from log_functions import count_log_levels,write_json_report
@pytest.mark.parametrize(
    "lines, expected",
    [
        (
            ["2026-10-28 10:30:00 ERROR Database failed"],
            {
                "ERROR": 1,
                "INFO": 0,
                "WARNING": 0,
                "UNKNOWN": 0,
                "INVALID": 0
            }
        ),
        (
            ["2026-10-28 10:31:00 DEBUG Debug message"],
            {
                "ERROR": 0,
                "INFO": 0,
                "WARNING": 0,
                "UNKNOWN": 1,
                "INVALID": 0
            }
        ),
        (
            ["2026-10-28 10:32:00 WARNING Memory low"],
            {
                "ERROR": 0,
                "INFO": 0,
                "WARNING": 1,
                "UNKNOWN": 0,
                "INVALID": 0
            }
        ),
        (
            [""],
            {
                "ERROR": 0,
                "INFO": 0,
                "WARNING": 0,
                "UNKNOWN": 0,
                "INVALID": 0
            }
        ),
        (
            ["2026-15-40 10:33:00 ERROR Database failed"],
            {
                "ERROR": 0,
                "INFO": 0,
                "WARNING": 0,
                "UNKNOWN": 0,
                "INVALID": 1          
            }  
        ),
        (
            [
              "2026-10-28 10:30:00 ERROR Database failed",
              "2026-10-28 10:31:00 ERROR Connection failed",
              "2026-10-28 10:32:00 INFO Server started",
              "2026-10-28 10:33:00 WARNING Memory low",
              "2026-10-28 10:34:00 DEBUG Debug message"
            ],
            {
                "ERROR": 2,
                "INFO": 1,
                "WARNING": 1,
                "UNKNOWN": 1,
                "INVALID": 0
            }
        ),
        (
            [],
            {
                "ERROR": 0,
                "INFO": 0,
                "WARNING": 0,
                "UNKNOWN": 0,
                "INVALID": 0
            }
        ),
        (
            ["2026-10-28"],
            {
            "ERROR": 0,
            "INFO": 0,
            "WARNING": 0,
            "UNKNOWN": 0,
            "INVALID": 1
            }
        )



    ]
)
def test_count_log_levels(lines, expected):
    result = count_log_levels(lines)
    assert result == expected
def test_write_json_report(tmp_path):
    results = {
        "ERROR": 2,
        "INFO": 3,
        "WARNING": 1,
        "UNKNOWN": 0,
        "INVALID": 1
    }
    output_file =tmp_path / "report.json"
    write_json_report(results, output_file)
    import json 
    with open (output_file, encoding="utf-8") as file:
        actual = json.load(file)

    assert actual == results