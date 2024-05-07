
class SortingResults:

    # this simple function takes in a key from the dictionary (which is a final day result) and a desired target,
    # and it returns the distance from the key to the target
    @staticmethod
    def distance_from_target(key, target):
        return abs(key - target)

    # this function takes in the dictionary of results and the desired escape probability and sorts it by each
    # result's closeness to the desired escape probability, returning it as a sorted dictionary
    @staticmethod
    def sorting(final_day_results, desired_esc_prob):
        return dict(sorted(final_day_results.items(),
                           key=lambda item: SortingResults.distance_from_target(item[0], desired_esc_prob)))

    # this function takes a list of two sets of lambdas, and it compares each lambda value. If a lambda is lower
    # than the other, it is added to the lower bounds, while the other one is added to upper bounds
    @staticmethod
    def compare_lambdas(lambda_list):
        l_bounds = []
        u_bounds = []
        for lam in range(len(lambda_list[0])):
            if lambda_list[0][lam] > lambda_list[1][lam]:
                u_bounds.append(lambda_list[0][lam])
                l_bounds.append(lambda_list[1][lam])
            else:
                l_bounds.append(lambda_list[0][lam])
                u_bounds.append(lambda_list[1][lam])
        return [l_bounds, u_bounds]

    # this function first takes the dictionary of results and finds the 2 sets of lambdas closest to the target,
    # (one being higher than the target and one being lower). Then, for each lambda, it compares the lambdas from
    # the 2 sets and places the smaller one to the lower bound and the greater one to the upper bound, returning
    # a list with recommended lower bounds as the first value and recommended upper bounds as the second value.
    @staticmethod
    def recommended_bounds(final_res, desired_esc_prob):
        two_closest = []
        found = False
        two_closest.append(list(final_res.values())[0])
        if list(final_res.keys())[0] > desired_esc_prob:
            for result in final_res.keys():
                if result < desired_esc_prob:
                    two_closest.append(final_res.get(result))
                    found = True
                    break
            if not found:
                two_closest.append([0 for _ in range(len(two_closest[0]))])
        else:
            for result in final_res.keys():
                if result > desired_esc_prob:
                    two_closest.append(final_res.get(result))
                    found = True
                    break
            if not found:
                two_closest.append([1 for _ in range(len(two_closest[0]))])

        recommended = SortingResults.compare_lambdas(two_closest)
        return recommended


