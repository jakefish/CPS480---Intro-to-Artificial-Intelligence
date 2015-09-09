def calculate_results(wow_classes):

    """ Takes a list of WoWClass objects and determines the class that contains
        the highest rank from the quiz.
    """

    highest_rank = 0
    for wow_class_name, wow_class in wow_classes.items():
        if wow_class.class_rank >= highest_rank:
            highest_rank = wow_class.class_rank
            winning_class = wow_class.class_name
    return winning_class
