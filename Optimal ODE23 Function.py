# Finalized ODE23 function
def ode23(de_fcn, tspan, y0, tol, h0, maxh, theta):

    '''ODE 23 is an Numerical ODE method of Order two and three with adaptive step size.
    This Second Order method is implemented in terms of the Trapezoid Method while that of 
    of the Third Order is of the Runge-Kutta method. 
    
    This final model incorporates the 
    optimal step sizing procedure based on the Morris-Lecar Biological Neuron Model. 

    This function evaluates the Differential Equation (de_fcn), given a time span (tspan), 
    initial value condition (y0), error tolerence (tol), intial step size (h0) and maximum step 
    size maxh.

    The Theta Variable has been identified as being the optimal growth and contraction value of
    the optimal step size. In prior implementations, this value is of .15. Theta = 1 + .15. Phi = 1 - .15. 
    '''

    # Initializing history lists
    t_history = [tspan[0]]
    y_history = [y0]
    a_history = [1]
    h_history = [h0]
    e_history = []

    # Initializing Variables
    f_evals = 0
    h = h0
    t = tspan[0]
    y = np.array(y0)
    alpha = 1
    
    # Looping until we reach tspan
    while t<=tspan[1]:

        # Midpoint Method
        k0, f_evals = de_fcn(t, y)
        k1, f_evals = de_fcn(t + 0.5*h, y + 0.5*h*k0)
        y_m = y + h*k1

        # Runge-Kutta Method
        k2, f_evals = de_fcn(t + .75*h, y + 0.75*h*k1)
        y_rk3 = y + h*(2*k0/9 + k1/3 + 4*k2/9)

        # Error and Gamma factors
        e = np.linalg.norm(y_m - y_rk3)
        gamma = (tol/e)**(1/3)

        e_history.append(e)


        # Step Size Error Analysis
        if e <= tol:
            # Tolerence is met: Acceptible Step Size -> Saving the step values
            y_history.append(y_rk3.tolist())
            t_history.append(t)

            y = y_rk3
            t = t + h
            h_opt = h * gamma * alpha

            # Identification of the next optimal h: this prevents alpha from growing in the instance that h_opt > maxh 
            if h_opt == min(h_opt, maxh):
                alpha = 1.15 * alpha
                h_opt = h * gamma * alpha
                h = h_opt

            else: 
                h = maxh

            # Appending history variables
            h_history.append(h_opt)
            a_history.append(alpha)

        # Tolerence has not been met: Unacceptiable Step Size -> reattempting step size with alpha contraction
        else:
            alpha = .85 * alpha
            h_opt = h * gamma * alpha
            h = min(h_opt, maxh)

            # Appending Step Variables
            a_history.append(alpha)
            h_history.append(h_opt)
    
    return np.array(y_history), np.array(t_history), f_evals, a_history, h_history, e_history
