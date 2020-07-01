import csv

class Seating_matrix:


    def __init__(self, in_file):
        self.seats = []
        self.adj_seats = []
        self.seat_coords = []
        self.in_file = in_file

    def get_seats(self):
        self.col_num = 0
        self.row_num = 0

        with open(self.in_file, 'r') as f:

            file_reader = csv.reader(f)
            id_row = next(file_reader)
            size_row = next(file_reader)

            if id_row[0] == "courseid":
                self.courseid = id_row[1]

            self.col_num = len(size_row) -1


            for row in file_reader:
                if self.col_num != len(row[1:]):
                    print("CSV IS FORMATTED WRONG (COL)")
                else:
                    self.seats.append(row[1:])
                self.row_num += 1



            if self.row_num != len(self.seats):
                print("CSV IF FORMATTED WRONG (ROW)")


    @staticmethod
    def make_null_matrix(matrix):
        null_matrix = []

        null_matrix_outer_row = []
        for i in range(1, len(matrix[0])+3):
            null_matrix_outer_row.append(None)

        null_matrix.append(null_matrix_outer_row)

        for row in matrix:
            null_matrix_inner_row = []
            null_matrix_inner_row.append(None)

            for item in row:
                null_matrix_inner_row.append(item)

            null_matrix_inner_row.append(None)
            null_matrix.append(null_matrix_inner_row)

        null_matrix.append(null_matrix_outer_row)

        return null_matrix

    def make_adj_seats(self):
        null_matrix = Seating_matrix.make_null_matrix(self.seats)

        for i in range(len(null_matrix)):
            for j in range(len(null_matrix[0])):
                if null_matrix[i][j] == None:
                    continue


                adj_seats_seat = []
                adj_seats_seat.append(null_matrix[i][j])

                for k in range(-1,2,1):
                    for l in range(-1,2,1):
                        
                        if null_matrix[i+k][j+l] == null_matrix[i][j] or null_matrix[i+k][j+l] == None:
                            continue
                        else:
                            adj_seats_seat.append(null_matrix[i+k][j+l])

                self.adj_seats.append(adj_seats_seat)












adj = Seating_matrix('course01.csv')
adj.get_seats()
#print(adj.seats)
seat = adj.seats

adj.make_adj_seats()
print(adj.adj_seats)
