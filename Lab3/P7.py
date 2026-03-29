preturi = [100, None, 250, None, 80, 320]

preturi_reduse = list(
    map(
        lambda p: p * 0.9,
        filter(lambda p: p is not None, preturi)
    )
)

print(preturi_reduse)