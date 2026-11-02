from main import count_log_levels


def test_count_log_levels():
    lines = [
        "2026-10-28 10:30:00 ERROR Database failed",
        "2026-10-28 10:31:00 INFO Server started",
        "2026-10-28 10:32:00 WARNING Memory low",
        "2026-10-28 10:33:00 DEBUG Debug message",
        "",
        "INVALID LINE",
        "2026-13-28 10:34:00 ERROR Wrong date"
    ]

    result = count_log_levels(lines)

    expected = {
        "ERROR": 1,
        "INFO": 1,
        "WARNING": 1,
        "UNKNOWN": 1,
        "INVALID": 2
    }

    assert result == expected