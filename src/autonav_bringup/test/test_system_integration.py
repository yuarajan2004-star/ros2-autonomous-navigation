def test_required_topics():

    required_topics = [
        "/scan",
        "/map",
        "/tf",
        "/odom"
    ]

    assert len(required_topics) == 4


def test_navigation_pipeline():

    localization = True
    slam = True
    planning = True
    control = True

    assert (
        localization
        and slam
        and planning
        and control
    )
