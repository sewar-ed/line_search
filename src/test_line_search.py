# import unittest
# import numpy as np
# from src.line_search_algorithm import line_search
# from src.utils import plot_contour, plot_function_values
# class TestUnconstrainedMin(unittest.TestCase):

#     def setUp(self):
#         self.methods = ["gradient_descent", "newtons_method"]
#         self.A = []
#         self.b=[]
#         self.c=0
#         self.obj_tol=10^-12
#         self.param_tol=10^-8
#         self.max_iter=1000
#         self.flag=True

#     def test_methods(self):
#         for example in self.examples:
#             path_history=[]
#             function_values = {}
#             # Perform minimization
#             _, history_gd, _, history_n = line_search(self.A, self.b, self.c, alpha=0.01, max_iter=1000, tol=1e-6)
#             #Create contour plot
#             name="gradient_descent"
#             path_history.append((name,history_gd))
#             #Create contour plot
#             name="newton"
#             path_history.append((name,history_n))

#             plot_contour(example,(-2, 2),(-2, 2),path_history)

#             # Store function values for plot
#             function_values["gradient_descent"] = history_gd
#             function_values["newton"] = history_n

#             # Create function values plot
#             plot_function_values(function_values)

# if __name__ == "__main__":
#     unittest.main()