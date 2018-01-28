def branch_and_bound(g):
    def get_lb():
        pass
    pass



if __name__ == '__main__':
    graph = {
        1: {
            2: 3,
            3: 1,
            4: 5,
            5: 8
        },
        2: {
            1: 3,
            3: 6,
            4: 7,
            5: 9
        },
        3: {
            1: 1,
            2: 6,
            4: 4,
            5: 2
        },
        4: {
            1: 5,
            2: 7,
            3: 4,
            5: 3,
        },
        5: {
            1: 8,
            2: 9,
            3: 2,
            4: 3,
        }
    }
    branch_and_bound(graph)