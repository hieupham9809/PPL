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


    # Visit a parse tree produced by MPParser#manydeclr.
    def visitManydeclr(self, ctx:MPParser.ManydeclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#declaration.
    def visitDeclaration(self, ctx:MPParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#varDec.
    def visitVarDec(self, ctx:MPParser.VarDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#typeMP.
    def visitTypeMP(self, ctx:MPParser.TypeMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#idList.
    def visitIdList(self, ctx:MPParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcDec.
    def visitFuncDec(self, ctx:MPParser.FuncDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paramDec.
    def visitParamDec(self, ctx:MPParser.ParamDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#smList.
    def visitSmList(self, ctx:MPParser.SmListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#body.
    def visitBody(self, ctx:MPParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmtType.
    def visitStmtType(self, ctx:MPParser.StmtTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement.
    def visitStatement(self, ctx:MPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignment.
    def visitAssignment(self, ctx:MPParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#call.
    def visitCall(self, ctx:MPParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expressionList.
    def visitExpressionList(self, ctx:MPParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnMP.
    def visitReturnMP(self, ctx:MPParser.ReturnMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression.
    def visitExpression(self, ctx:MPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp.
    def visitExp(self, ctx:MPParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp1.
    def visitExp1(self, ctx:MPParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp2.
    def visitExp2(self, ctx:MPParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp0.
    def visitExp0(self, ctx:MPParser.Exp0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp3.
    def visitExp3(self, ctx:MPParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp4.
    def visitExp4(self, ctx:MPParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#operand.
    def visitOperand(self, ctx:MPParser.OperandContext):
        return self.visitChildren(ctx)



del MPParser