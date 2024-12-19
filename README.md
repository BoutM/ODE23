# ODE23
Exploring the Optimal Step Size of the ODE23 function with adaptive time stepping. 

In-depth description:

After exploring the ODE23 function with adaptive step sizes sith a class colleague, some exploring lead us to notice that given the ODE23 fuction provided, the Alpha value may grow uncontrollably within the while loop of the function when the optimal step size (h_opt) is taken as the maximum step size, which is user defined in the ODE23 function. 

This lead me to explore the idea of an optimal growth/contraction factor for the ODE23 method, based on the Moris-Lecar Neuron Model. This included the extraction of additional history variables from the function, their analysis and subsequent conclusion on which $\theta$ and $\phi$ values would reduce the residual errors of the ODE23 function. 

My analysis concludes that $\theta = 1.15$ and $\phi = .85$ are the optimal growth and contraction factors (respectively) for the ODE 23 function. 

This conlusion is based on the simply symetric approach of $\theta = 1 + factor$, $\phi = 1 - factor$. Future investigation should include the analysis of asymetric factors. That is, $\theta - -1 \ne \phi$, which is what has been original presented in the Base ODE23 function.

