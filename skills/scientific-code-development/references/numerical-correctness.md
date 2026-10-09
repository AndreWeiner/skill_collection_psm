# Numerical correctness

Define units/dimensions, array/field association, layout, indexing, normalization,
weighting and boundary conventions. Confirm which axes are reduced and whether
statistics are local/global, weighted/unweighted, or conditional on masking.
Do not accept shape-compatible broadcasting as proof of the intended operation.

Choose algorithms with attention to conditioning, cancellation, accumulation,
overflow/underflow and convergence. Use established stable formulations and
solvers; do not introduce explicit inverses or ad hoc numerical methods merely
to shorten code. Reduced precision, approximation, fast-math or altered reduction
ordering require evidence that the scientific accuracy requirements still hold.

Distinguish dimensional/structural validity from physical or mathematical
validity: a compatible array may contain nonfinite values, invalid weights,
zero denominators, singular systems or insufficient samples. Choose appropriate
handling and tolerances from the problem and precision, not a universal epsilon.
Do not silently replace invalid values with zeros to make tests pass.

Verify by an analytic/manufactured result, a mathematically suitable invariant,
or an independent trusted method. Include a discriminating example: nonuniform
weights, nonsymmetric/non-square shapes, known null spaces, or boundary effects
as relevant. Separate residual/error, convergence and conditioning checks;
agreement with one implementation can reproduce the same error.

Document changed numerical conventions and support claims. A small test proves
only its exercised path, not general physical validity, causal interpretation,
or accuracy across untested parameter regimes.
