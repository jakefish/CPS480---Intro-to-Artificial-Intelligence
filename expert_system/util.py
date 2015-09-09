def calculate_results(wow_classes):
    highest_rank = 0
    for wow_class in wow_classes:
        if wow_class.class_rank >= highest_rank:
            highest_rank = wow_class.class_rank
            winning_class = wow_class.class_name
    return winning_class
