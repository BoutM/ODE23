# ODE23
Exploring the Optimal Step Size of the ODE23 function with adaptive time stepping. 

In-depth description:

After exploring the ODE23 function with adaptive step sizes sith a class colleague, some exploring lead us to notice that given the ODE23 fuction provided, the Alpha value may grow uncontrollably within the while loop of the function when the optimal step size (h_opt) is taken as the maximum step size, which is user defined.

This lead me to explore the idea of an optimal growth/contraction factor (which I refer to as $\theta$ and $\phi$) for the ODE23 method, based on the Moris-Lecar Neuron Model. This explorational includes the extraction of additional history variables from the function and their analysis, changes to the h_opt methodology and its impacts as well as a conclusion on which $\theta$ and $\phi$ values are optimal to reduce the residual errors of the ODE23 function step sizes. 

My analysis concludes that $\theta = 1.15$ and $\phi = .85$ are the optimal growth and contraction factors (respectively) for the ODE 23 function. Please note that this indicates that $\alpha = \alpha \times \theta$ for an acceptible step size, while $\alpha = \alpha \times \phi$ for an unacceptiable step size. Furhtermore, A stopping criteria has been implemented for $\alpha$ when $h_opt > maxh$, preventing $\alpha$ from growing in cases where $h_max$ is selected as the optimal step size.

The conlusion on the optimal $\theta$ and $\phi$ variables are based on the simply symmetric approach of $\theta = 1 + factor$, $\phi = 1 - factor$. Future investigation should investigate an asymmetric factor. That is, $\theta -1 \ne 1- \phi$. 

