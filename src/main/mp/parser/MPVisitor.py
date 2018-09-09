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


    # Visit a parse tree produced by MPParser#varDec.
    def visitVarDec(self, ctx:MPParser.VarDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listOfDecls.
    def visitListOfDecls(self, ctx:MPParser.ListOfDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listOfDecls1.
    def visitListOfDecls1(self, ctx:MPParser.ListOfDecls1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listOfType.
    def visitListOfType(self, ctx:MPParser.ListOfTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listID.
    def visitListID(self, ctx:MPParser.ListIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listID1.
    def visitListID1(self, ctx:MPParser.ListID1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#types.
    def visitTypes(self, ctx:MPParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arraycp.
    def visitArraycp(self, ctx:MPParser.ArraycpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arrayType.
    def visitArrayType(self, ctx:MPParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcDec.
    def visitFuncDec(self, ctx:MPParser.FuncDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procDec.
    def visitProcDec(self, ctx:MPParser.ProcDecContext):
        return self.visitChildren(ctx)



del MPParser