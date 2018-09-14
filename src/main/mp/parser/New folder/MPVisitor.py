# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#declaration.
    def visitDeclaration(self, ctx:MPParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#var_decl.
    def visitVar_decl(self, ctx:MPParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_decls.
    def visitList_decls(self, ctx:MPParser.List_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#decl.
    def visitDecl(self, ctx:MPParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_ID.
    def visitList_ID(self, ctx:MPParser.List_IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#func_decl.
    def visitFunc_decl(self, ctx:MPParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#param_list.
    def visitParam_list(self, ctx:MPParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#param_list1.
    def visitParam_list1(self, ctx:MPParser.Param_list1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#param.
    def visitParam(self, ctx:MPParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procedure_decl.
    def visitProcedure_decl(self, ctx:MPParser.Procedure_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#mptype.
    def visitMptype(self, ctx:MPParser.MptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primitive_type.
    def visitPrimitive_type(self, ctx:MPParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_type.
    def visitCompound_type(self, ctx:MPParser.Compound_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arraylit.
    def visitArraylit(self, ctx:MPParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr.
    def visitExpr(self, ctx:MPParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr1.
    def visitExpr1(self, ctx:MPParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr2.
    def visitExpr2(self, ctx:MPParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr3.
    def visitExpr3(self, ctx:MPParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr4.
    def visitExpr4(self, ctx:MPParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr5.
    def visitExpr5(self, ctx:MPParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr6.
    def visitExpr6(self, ctx:MPParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#operand.
    def visitOperand(self, ctx:MPParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#array_elmt.
    def visitArray_elmt(self, ctx:MPParser.Array_elmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#func_call.
    def visitFunc_call(self, ctx:MPParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_expr.
    def visitList_expr(self, ctx:MPParser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_expr1.
    def visitList_expr1(self, ctx:MPParser.List_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement.
    def visitStatement(self, ctx:MPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:MPParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#if_stmt.
    def visitIf_stmt(self, ctx:MPParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#while_stmt.
    def visitWhile_stmt(self, ctx:MPParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#for_stmt.
    def visitFor_stmt(self, ctx:MPParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#break_stmt.
    def visitBreak_stmt(self, ctx:MPParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MPParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#return_stmt.
    def visitReturn_stmt(self, ctx:MPParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_stmt.
    def visitCompound_stmt(self, ctx:MPParser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_stmt.
    def visitList_stmt(self, ctx:MPParser.List_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_stmt1.
    def visitList_stmt1(self, ctx:MPParser.List_stmt1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#call_stmt.
    def visitCall_stmt(self, ctx:MPParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#with_stmt.
    def visitWith_stmt(self, ctx:MPParser.With_stmtContext):
        return self.visitChildren(ctx)



del MPParser