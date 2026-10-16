import src.lam as lam
import src.ski as ski

##########
# PART 3 #
##########
# TASK: Implement the below function `tran`.
# You can define helper functions outside `tran` and use them inside `tran`.

"""
tran:
translates the lam.Expr "e" into the equivalent ski.Expr.
"""
def tran(e: lam.Expr) -> ski.Expr:
    # BEGIN_YOUR_CODE
    if isinstance(e, lam.Var):
        return ski.Var(e.s)
    if isinstance(e, lam.Lam):
        return ski_abstract(tran(e.e), ski.Var(e.s))
    return ski.App(tran(e.e1), tran(e.e2))
    # END_YOUR_CODE


"""
ski_abstract:
Applies the abstraction algorithm to ski.Expr "e" wrt ski.Var x.
"""
def ski_abstract(e: ski.Expr, x: ski.Var) -> ski.Expr:
    if e == x:
        return ski.I()
    if not ski_x_in_e(e, x):
        return ski.App(ski.K(), e)
    return ski.App(ski.App(ski.S(), ski_abstract(e.e1, x)), ski_abstract(e.e2, x))

"""
ski_x_in_e:
Returns true the ski.Var "x" exists in the ski.Expr "e", and false otherwise.
"""
def ski_x_in_e(e: ski.Expr, x: ski.Var) -> bool:
    if e == x:
        return True
    if isinstance(e, ski.S) or isinstance(e, ski.K) or isinstance(e, ski.I) or isinstance(e, ski.Var):
        return False
    return ski_x_in_e(e.e1, x) or ski_x_in_e(e.e2, x)