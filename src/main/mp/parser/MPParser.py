# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\6\2\36\n\2\r\2\16\2\37\3\3\3\3\3\3\5\3%\n\3\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\62\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t?\n\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\5\nF\n\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\2")
        buf.write("\2\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\3\3\2\27\32\2")
        buf.write("R\2\35\3\2\2\2\4$\3\2\2\2\6&\3\2\2\2\b)\3\2\2\2\n\61\3")
        buf.write("\2\2\2\f\63\3\2\2\2\16\67\3\2\2\2\20>\3\2\2\2\22E\3\2")
        buf.write("\2\2\24G\3\2\2\2\26P\3\2\2\2\30R\3\2\2\2\32T\3\2\2\2\34")
        buf.write("\36\5\4\3\2\35\34\3\2\2\2\36\37\3\2\2\2\37\35\3\2\2\2")
        buf.write("\37 \3\2\2\2 \3\3\2\2\2!%\5\6\4\2\"%\5\30\r\2#%\5\32\16")
        buf.write("\2$!\3\2\2\2$\"\3\2\2\2$#\3\2\2\2%\5\3\2\2\2&\'\7\22\2")
        buf.write("\2\'(\5\b\5\2(\7\3\2\2\2)*\5\f\7\2*+\5\n\6\2+\t\3\2\2")
        buf.write("\2,-\7\60\2\2-.\5\f\7\2./\5\n\6\2/\62\3\2\2\2\60\62\7")
        buf.write("\60\2\2\61,\3\2\2\2\61\60\3\2\2\2\62\13\3\2\2\2\63\64")
        buf.write("\5\16\b\2\64\65\7\64\2\2\65\66\5\22\n\2\66\r\3\2\2\2\67")
        buf.write("8\7 \2\289\5\20\t\29\17\3\2\2\2:;\7\61\2\2;<\7 \2\2<?")
        buf.write("\5\20\t\2=?\3\2\2\2>:\3\2\2\2>=\3\2\2\2?\21\3\2\2\2@F")
        buf.write("\7\30\2\2AF\7\31\2\2BF\7\27\2\2CF\7\32\2\2DF\5\24\13\2")
        buf.write("E@\3\2\2\2EA\3\2\2\2EB\3\2\2\2EC\3\2\2\2ED\3\2\2\2F\23")
        buf.write("\3\2\2\2GH\7\25\2\2HI\7\62\2\2IJ\7+\2\2JK\7\65\2\2KL\7")
        buf.write("+\2\2LM\7\63\2\2MN\7\26\2\2NO\5\26\f\2O\25\3\2\2\2PQ\t")
        buf.write("\2\2\2Q\27\3\2\2\2RS\7 \2\2S\31\3\2\2\2TU\7 \2\2U\33\3")
        buf.write("\2\2\2\7\37$\61>E")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'*'", 
                     "'<>'", "'<'", "'<='", "'-'", "'/'", "'='", "'>'", 
                     "'>='", "<INVALID>", "<INVALID>", "<INVALID>", "'('", 
                     "')'", "';'", "','", "'['", "']'", "':'", "'..'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", 
                      "DO", "IF", "THEN", "ELSE", "RETURNS", "WHILE", "BEGIN", 
                      "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", 
                      "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", 
                      "NOT", "AND", "OR", "DIV", "MOD", "ID", "ADDOP", "MULOP", 
                      "NEQOP", "LTOP", "LTEOP", "SUBOP", "DIVOP", "EQOP", 
                      "GTOP", "GTEOP", "INTLIT", "REALIT", "STRLIT", "LB", 
                      "RB", "SEMI", "COMMA", "LSB", "RSB", "COLON", "DDOT", 
                      "WS", "BLOCKCOM_B", "BLOCKCOM_P", "LINECOM", "ERROR_CHAR", 
                      "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_varDec = 2
    RULE_listOfDecls = 3
    RULE_listOfDecls1 = 4
    RULE_listOfType = 5
    RULE_listID = 6
    RULE_listID1 = 7
    RULE_types = 8
    RULE_arraycp = 9
    RULE_arrayType = 10
    RULE_funcDec = 11
    RULE_procDec = 12

    ruleNames =  [ "program", "declaration", "varDec", "listOfDecls", "listOfDecls1", 
                   "listOfType", "listID", "listID1", "types", "arraycp", 
                   "arrayType", "funcDec", "procDec" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    FOR=3
    TO=4
    DOWNTO=5
    DO=6
    IF=7
    THEN=8
    ELSE=9
    RETURNS=10
    WHILE=11
    BEGIN=12
    END=13
    FUNCTION=14
    PROCEDURE=15
    VAR=16
    TRUE=17
    FALSE=18
    ARRAY=19
    OF=20
    REAL=21
    BOOLEAN=22
    INTEGER=23
    STRING=24
    NOT=25
    AND=26
    OR=27
    DIV=28
    MOD=29
    ID=30
    ADDOP=31
    MULOP=32
    NEQOP=33
    LTOP=34
    LTEOP=35
    SUBOP=36
    DIVOP=37
    EQOP=38
    GTOP=39
    GTEOP=40
    INTLIT=41
    REALIT=42
    STRLIT=43
    LB=44
    RB=45
    SEMI=46
    COMMA=47
    LSB=48
    RSB=49
    COLON=50
    DDOT=51
    WS=52
    BLOCKCOM_B=53
    BLOCKCOM_P=54
    LINECOM=55
    ERROR_CHAR=56
    UNCLOSE_STRING=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MPParser.DeclarationContext,i)


        def getRuleIndex(self):
            return MPParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.declaration()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MPParser.VAR or _la==MPParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDec(self):
            return self.getTypedRuleContext(MPParser.VarDecContext,0)


        def funcDec(self):
            return self.getTypedRuleContext(MPParser.FuncDecContext,0)


        def procDec(self):
            return self.getTypedRuleContext(MPParser.ProcDecContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MPParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.varDec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.funcDec()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.procDec()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarDecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MPParser.VAR, 0)

        def listOfDecls(self):
            return self.getTypedRuleContext(MPParser.ListOfDeclsContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_varDec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDec" ):
                return visitor.visitVarDec(self)
            else:
                return visitor.visitChildren(self)




    def varDec(self):

        localctx = MPParser.VarDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(MPParser.VAR)
            self.state = 37
            self.listOfDecls()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListOfDeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listOfType(self):
            return self.getTypedRuleContext(MPParser.ListOfTypeContext,0)


        def listOfDecls1(self):
            return self.getTypedRuleContext(MPParser.ListOfDecls1Context,0)


        def getRuleIndex(self):
            return MPParser.RULE_listOfDecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListOfDecls" ):
                return visitor.visitListOfDecls(self)
            else:
                return visitor.visitChildren(self)




    def listOfDecls(self):

        localctx = MPParser.ListOfDeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_listOfDecls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.listOfType()
            self.state = 40
            self.listOfDecls1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListOfDecls1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def listOfType(self):
            return self.getTypedRuleContext(MPParser.ListOfTypeContext,0)


        def listOfDecls1(self):
            return self.getTypedRuleContext(MPParser.ListOfDecls1Context,0)


        def getRuleIndex(self):
            return MPParser.RULE_listOfDecls1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListOfDecls1" ):
                return visitor.visitListOfDecls1(self)
            else:
                return visitor.visitChildren(self)




    def listOfDecls1(self):

        localctx = MPParser.ListOfDecls1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listOfDecls1)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(MPParser.SEMI)
                self.state = 43
                self.listOfType()
                self.state = 44
                self.listOfDecls1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(MPParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListOfTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listID(self):
            return self.getTypedRuleContext(MPParser.ListIDContext,0)


        def COLON(self):
            return self.getToken(MPParser.COLON, 0)

        def types(self):
            return self.getTypedRuleContext(MPParser.TypesContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_listOfType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListOfType" ):
                return visitor.visitListOfType(self)
            else:
                return visitor.visitChildren(self)




    def listOfType(self):

        localctx = MPParser.ListOfTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_listOfType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.listID()
            self.state = 50
            self.match(MPParser.COLON)
            self.state = 51
            self.types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListIDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def listID1(self):
            return self.getTypedRuleContext(MPParser.ListID1Context,0)


        def getRuleIndex(self):
            return MPParser.RULE_listID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListID" ):
                return visitor.visitListID(self)
            else:
                return visitor.visitChildren(self)




    def listID(self):

        localctx = MPParser.ListIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_listID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(MPParser.ID)
            self.state = 54
            self.listID1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListID1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MPParser.COMMA, 0)

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def listID1(self):
            return self.getTypedRuleContext(MPParser.ListID1Context,0)


        def getRuleIndex(self):
            return MPParser.RULE_listID1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListID1" ):
                return visitor.visitListID1(self)
            else:
                return visitor.visitChildren(self)




    def listID1(self):

        localctx = MPParser.ListID1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_listID1)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(MPParser.COMMA)
                self.state = 57
                self.match(MPParser.ID)
                self.state = 58
                self.listID1()
                pass
            elif token in [MPParser.COLON]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MPParser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MPParser.INTEGER, 0)

        def REAL(self):
            return self.getToken(MPParser.REAL, 0)

        def STRING(self):
            return self.getToken(MPParser.STRING, 0)

        def arraycp(self):
            return self.getTypedRuleContext(MPParser.ArraycpContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = MPParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_types)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(MPParser.BOOLEAN)
                pass
            elif token in [MPParser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(MPParser.INTEGER)
                pass
            elif token in [MPParser.REAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(MPParser.REAL)
                pass
            elif token in [MPParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.match(MPParser.STRING)
                pass
            elif token in [MPParser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.arraycp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArraycpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MPParser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MPParser.LSB, 0)

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.INTLIT)
            else:
                return self.getToken(MPParser.INTLIT, i)

        def DDOT(self):
            return self.getToken(MPParser.DDOT, 0)

        def RSB(self):
            return self.getToken(MPParser.RSB, 0)

        def OF(self):
            return self.getToken(MPParser.OF, 0)

        def arrayType(self):
            return self.getTypedRuleContext(MPParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_arraycp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraycp" ):
                return visitor.visitArraycp(self)
            else:
                return visitor.visitChildren(self)




    def arraycp(self):

        localctx = MPParser.ArraycpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arraycp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(MPParser.ARRAY)
            self.state = 70
            self.match(MPParser.LSB)
            self.state = 71
            self.match(MPParser.INTLIT)
            self.state = 72
            self.match(MPParser.DDOT)
            self.state = 73
            self.match(MPParser.INTLIT)
            self.state = 74
            self.match(MPParser.RSB)
            self.state = 75
            self.match(MPParser.OF)
            self.state = 76
            self.arrayType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MPParser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MPParser.INTEGER, 0)

        def REAL(self):
            return self.getToken(MPParser.REAL, 0)

        def STRING(self):
            return self.getToken(MPParser.STRING, 0)

        def getRuleIndex(self):
            return MPParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MPParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arrayType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.REAL) | (1 << MPParser.BOOLEAN) | (1 << MPParser.INTEGER) | (1 << MPParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncDecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def getRuleIndex(self):
            return MPParser.RULE_funcDec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDec" ):
                return visitor.visitFuncDec(self)
            else:
                return visitor.visitChildren(self)




    def funcDec(self):

        localctx = MPParser.FuncDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcDec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(MPParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcDecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def getRuleIndex(self):
            return MPParser.RULE_procDec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcDec" ):
                return visitor.visitProcDec(self)
            else:
                return visitor.visitChildren(self)




    def procDec(self):

        localctx = MPParser.ProcDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_procDec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(MPParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





