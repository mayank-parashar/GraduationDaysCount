class GraduationDays:
    def __init__(self, graduation_days):
        self.graduation_days = graduation_days

    def get_missing_ceremony_probability(self, max_miss_days):
        # creating an array of size 4+1, this will used to save result from past day
        dp_memo = [1] * (max_miss_days + 1)
        dp_memo[max_miss_days] = 0
        # this will used to save result for current day we are calculating results
        curr_memo = [0] * (max_miss_days + 1)

        for i in range(1, self.graduation_days + 1):
            curr_memo = [0] * (max_miss_days + 1)
            for j in range(max_miss_days - 1, -1, -1):
                # no of ways to attend class will for maximum j days allowed to skip will be calculate
                # by sum of no. of valid classes for past day and
                # number of ways to miss last day for with max_miss_days is j
                curr_memo[j] = dp_memo[0] + dp_memo[j + 1]

            curr_memo, dp_memo = dp_memo, curr_memo

        valid_classes_count = dp_memo[0]  # number of valid way to attend classes
        missed_class_count = curr_memo[1]  # number of way to miss last day

        return f"{missed_class_count}/{valid_classes_count}"


if __name__ == "__main__":
    graduation_days = int(input("number of days left in graduation ceremony"))
    missing_ceremony_probability = GraduationDays(
        graduation_days
    ).get_missing_ceremony_probability(max_miss_days=4)
    print(missing_ceremony_probability)
