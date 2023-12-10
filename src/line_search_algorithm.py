import numpy as np

def quadratic_function(x, A, b, c):
    #the function at x
    return 0.5 * np.dot(np.dot(x.T, A), x) - np.dot(b.T, x) + c

def calc_grad(x,A,b):
    #gradient of f at x
    return np.dot(A,x)- b

def line_search(A, b, c, alpha=0.01, max_iter=1000, tol=1e-6):
    #return sol
    gd_op, gd_path=gradient_descent(A, b, c, alpha, max_iter, tol)

    n_op, n_path=newton_method(A, b, c, alpha, max_iter, tol)

    return gd_op, gd_path, n_op,n_path

def gradient_descent(A, b, c, alpha=0.01, max_iter=1000, tol=1e-6):
    #initial value for x
    x_op= np.ones(len(b))
    path=[]

    for iter in range(max_iter):
        #append to path to plot later
        path.append((iter,x_op,quadratic_function(x_op, A, b, c)))
        
        grad=calc_grad(x_op, A, b)
        x_op -= alpha*grad

        #check convergence
        if np.linalg.norm(grad) < tol:
            #stop the search 
            break
    #return optimal solution and path gd took
    return x_op, path

def newton_method(A, b, c, alpha=0.01, max_iter=1000, tol=1e-6): 
    x_prev= np.ones(len(b)) #initial "guess"
    path=[]

    for iter in range(max_iter):
        path.append((iter,x_prev,quadratic_function(x_prev, A, b, c)))

        grad = calc_grad(x_prev, A, b)
        #calc step/direction of change by solving linear system
        hessian_inv_grad = np.linalg.solve(A, grad) #Hessain of Quad funcs is A
        x_new = x_prev - alpha*hessian_inv_grad

        # Check for convergence
        if np.linalg.norm(x_new - x_prev) < tol:
            break

        x_prev = x_new
    
    return x_prev, path
    




