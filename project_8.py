import numpy as np

class NumpyAnalyzer:
    def __init__(self):
        self.array1 = None
        self.array2 = None
        self.array3 = None

    def run(self):
        print('Welcome to Numpy Analyzer!')
        while True:
            print('\nChoose an option:')
            print('1. Create a numpy array')
            print('2. Perform mathematical operations')
            print('3. Combine or split arrays')
            print('4. Search, Sort or Filter arrays')
            print('5. Compute aggregates and statistics')
            print('6. Exit')
            a = int(input('Enter your choice: '))

            if a == 1:
                print('\nSelect the type of array to create:')
                print('1. 1D Array')
                print('2. 2D Array')
                print('3. 3D Array')
                choice = int(input('Enter your choice: '))
                if choice == 1:
                    arr = input('Enter elements separated by comma: ')
                    self.array1 = np.array([int(x) for x in arr.split(',')])
                    print('Array created successfully:')
                    print(self.array1)
                    while True:
                        print('\nChoose an operation:')
                        print('1. Indexing')
                        print('2. Slicing')
                        print('3. Go back')
                        b = int(input('Enter your choice: '))
                        if b == 1:
                            i = int(input('Enter index: '))
                            print(self.array1[i])
                        elif b == 2:
                            start = int(input('Start: '))
                            end = int(input('End: '))
                            print(self.array1[start:end])
                        elif b == 3:
                            break

                elif choice == 2:
                    rows = int(input('Enter number of rows: '))
                    cols = int(input('Enter number of columns: '))
                    arr = input(f'Enter {rows*cols} elements: ')
                    flat = [int(x) for x in arr.split(',')]
                    if len(flat) == rows * cols:
                        self.array2 = np.array(flat).reshape(rows, cols)
                        print('Array created successfully:')
                        print(self.array2)
                        while True:
                            print('\nChoose an operation:')
                            print('1. Indexing')
                            print('2. Slicing')
                            print('3. Go back')
                            c = int(input('Enter your choice: '))
                            if c == 1:
                                r = int(input('Row index: '))
                                col = int(input('Column index: '))
                                print(self.array2[r, col])
                            elif c == 2:
                                rs = int(input('Row start: '))
                                re = int(input('Row end: '))
                                cs = int(input('Column start: '))
                                ce = int(input('Column end: '))
                                print(self.array2[rs:re, cs:ce])
                            elif c == 3:
                                break
                    else:
                        print("Incorrect number of elements!")

                elif choice == 3:
                    blocks = int(input('Blocks: '))
                    rows = int(input('Rows: '))
                    cols = int(input('Columns: '))
                    arr = input(f'Enter {blocks*rows*cols} elements: ')
                    flat = [int(x) for x in arr.split(',')]
                    if len(flat) == blocks * rows * cols:
                        self.array3 = np.array(flat).reshape(blocks, rows, cols)
                        print('Array created successfully:')
                        print(self.array3)
                        while True:
                            print('\nChoose an operation:')
                            print('1. Indexing')
                            print('2. Slicing')
                            print('3. Go back')
                            d = int(input('Enter your choice: '))
                            if d == 1:
                                b = int(input('Block: '))
                                r = int(input('Row: '))
                                c = int(input('Column: '))
                                print(self.array3[b, r, c])
                            elif d == 2:
                                bs = int(input('Block start: '))
                                be = int(input('Block end: '))
                                rs = int(input('Row start: '))
                                re = int(input('Row end: '))
                                cs = int(input('Column start: '))
                                ce = int(input('Column end: '))
                                print(self.array3[bs:be, rs:re, cs:ce])
                            elif d == 3:
                                break
                    else:
                        print("Incorrect number of elements!")

            elif a == 2:
                print('\nChoose mathematical operation:')
                print('1. Add')
                print('2. Subtract')
                print('3. Multiply')
                print('4. Divide')
                op = int(input('Enter your choice: '))

                print('Choose array:')
                print('1. 1D array')
                print('2. 2D array')
                print('3. 3D array')
                ch = int(input('Enter your choice: '))
                val = int(input('Enter value: '))

                if ch == 1 and self.array1 is not None:
                    if op == 1:
                        print(self.array1 + val)
                    elif op == 2:
                        print(self.array1 - val)
                    elif op == 3:
                        print(self.array1 * val)
                    elif op == 4:
                        print(self.array1 / val)
                    else:
                        print('Invalid operation choice.')
                elif ch == 2 and self.array2 is not None:
                    if op == 1:
                        print(self.array2 + val)
                    elif op == 2:
                        print(self.array2 - val)
                    elif op == 3:
                        print(self.array2 * val)
                    elif op == 4:
                        print(self.array2 / val)
                    else:
                        print('Invalid operation choice.')
                elif ch == 3 and self.array3 is not None:
                    if op == 1:
                        print(self.array3 + val)
                    elif op == 2:
                        print(self.array3 - val)
                    elif op == 3:
                        print(self.array3 * val)
                    elif op == 4:
                        print(self.array3 / val)
                    else:
                        print('Invalid operation choice.')
                else:
                    print("Selected array doesn't exist. Please create it first.")

            elif a == 3:
                print('\n1. Combine')
                print('2. Split')
                g = int(input('Enter your choice: '))
                print('Choose array:')
                print('1.1D array')
                print('2.2D array')
                print('3.3D array')
                ch = int(input('Enter your choice: '))
                if ch == 1 and self.array1 is not None:
                    if g == 1:
                        new = np.array([int(x) for x in input('Enter new array: ').split(',')])
                        print(np.concatenate((self.array1, new)))
                    elif g == 2:
                        s = int(input('Enter number of divisions: '))
                        print(np.split(self.array1, s))
                elif ch == 2 and self.array2 is not None:
                    if g == 1:
                        r = int(input('Rows: '))
                        c = int(input('Cols: '))
                        new = np.array([int(x) for x in input(f'Enter {r*c} elements: ').split(',')]).reshape(r, c)
                        print(np.concatenate((self.array2, new)))
                    elif g == 2:
                        print('1. Horizontal\n2. Vertical')
                        h = int(input('Enter choice: '))
                        s = int(input('Splits: '))
                        if h == 1:
                            print(np.hsplit(self.array2, s))
                        else:
                            print(np.vsplit(self.array2, s))
                elif ch == 3 and self.array3 is not None:
                    if g == 1:
                        b = int(input('Blocks: '))
                        r = int(input('Rows: '))
                        c = int(input('Cols: '))
                        new = np.array([int(x) for x in input(f'Enter {b*r*c} elements: ').split(',')]).reshape(b, r, c)
                        print(np.concatenate((self.array3, new)))
                    elif g == 2:
                        print('1. Split rows\n2. Split columns\n3. Split blocks')
                        i = int(input('Enter choice: '))
                        s = int(input('Splits: '))
                        if i == 1:
                            print(np.split(self.array3, s, axis=1))
                        elif i == 2:
                            print(np.split(self.array3, s, axis=2))
                        elif i == 3:
                            print(np.split(self.array3, s, axis=0))

            elif a == 4:
                print('\n1. Search\n2. Sort\n3. Filter')
                x = int(input('Enter your choice: '))
                print('Choose array:')
                print('1.1D array')
                print('2.2D array')
                print('3.3D array')
                ch = int(input('Enter your choice: '))
                if ch == 1 and self.array1 is not None:
                    if x == 1:
                        val = int(input('Enter value: '))
                        print(np.where(self.array1 == val))
                    elif x == 2:
                        print('1. Ascending\n2. Descending')
                        order = int(input('enter your choice: '))
                        print(np.sort(self.array1) if order == 1 else np.sort(self.array1)[::-1])
                    elif x == 3:
                        val = int(input('Filter > value: '))
                        print(self.array1[self.array1 > val])
                elif ch == 2 and self.array2 is not None:
                    if x == 1:
                        val = int(input('Enter value: '))
                        print(np.where(self.array2 == val))
                    elif x == 2:
                        print('1. Row-wise\n2. Column-wise')
                        y = int(input('Order: '))
                        print(np.sort(self.array2, axis=1 if y == 1 else 0))
                    elif x == 3:
                        val = int(input('Filter > value: '))
                        print(self.array2[self.array2 > val])
                elif ch == 3 and self.array3 is not None:
                    if x == 1:
                        val = int(input('Enter value: '))
                        print(np.where(self.array3 == val))
                    elif x == 2:
                        print('1. Block-wise\n2. Row-wise\n3. Column-wise')
                        y = int(input('Order: '))
                        print(np.sort(self.array3, axis=y - 1))
                    elif x == 3:
                        val = int(input('Filter > value: '))
                        print(self.array3[self.array3 > val])

            elif a == 5:
                print('\n1. Sum\n2. Mean\n3. Median\n4. Std Dev\n5. Variance\n6. Max\n7. Min')
                k = int(input('Enter your choice: '))
                print('Choose array:')
                print('1.1D array')
                print('2.2D array')
                print('3.3D array')
                ch = int(input('Enter your choice: '))
                if ch == 1:
                    arr = self.array1
                elif ch == 2:
                    arr = self.array2
                else:
                    arr = self.array3

                if arr is not None:
                    if k == 1: print(np.sum(arr))
                    elif k == 2: print(np.mean(arr))
                    elif k == 3: print(np.median(arr))
                    elif k == 4: print(np.std(arr))
                    elif k == 5: print(np.var(arr))
                    elif k == 6: print(np.max(arr))
                    elif k == 7: print(np.min(arr))
                else:
                    print('No array found!')

            elif a == 6:
                print('Thank you for using Numpy Analyzer!')
                break


# Create instance and run
app = NumpyAnalyzer()
app.run()