# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("\u0093\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\6\59\n\5\r\5\16\5:\3\6\6\6>\n\6")
        buf.write("\r\6\16\6?\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\f\6\fM\n\f\r\f\16\fN\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\17\7\17Z\n\17\f\17\16\17]\13\17\3\20\7\20`\n\20")
        buf.write("\f\20\16\20c\13\20\3\20\3\20\6\20g\n\20\r\20\16\20h\3")
        buf.write("\20\7\20l\n\20\f\20\16\20o\13\20\3\20\3\20\6\20s\n\20")
        buf.write("\r\20\16\20t\5\20w\n\20\3\20\3\20\5\20{\n\20\3\20\6\20")
        buf.write("~\n\20\r\20\16\20\177\5\20\u0082\n\20\3\21\3\21\3\21\3")
        buf.write("\21\6\21\u0088\n\21\r\21\16\21\u0089\3\21\3\21\3\22\3")
        buf.write("\22\3\23\3\23\3\24\3\24\2\2\25\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\2\33\2\35\16\37\17!\20")
        buf.write("#\21%\22\'\23\3\2\7\4\2C\\c|\3\2\62;\5\2\13\f\17\17\"")
        buf.write("\"\3\2c|\3\2))\2\u009f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\3)\3\2\2\2\5.\3\2\2\2\7\62\3\2\2\2\t")
        buf.write("8\3\2\2\2\13=\3\2\2\2\rA\3\2\2\2\17C\3\2\2\2\21E\3\2\2")
        buf.write("\2\23G\3\2\2\2\25I\3\2\2\2\27L\3\2\2\2\31R\3\2\2\2\33")
        buf.write("T\3\2\2\2\35V\3\2\2\2\37\u0081\3\2\2\2!\u0083\3\2\2\2")
        buf.write("#\u008d\3\2\2\2%\u008f\3\2\2\2\'\u0091\3\2\2\2)*\7o\2")
        buf.write("\2*+\7c\2\2+,\7k\2\2,-\7p\2\2-\4\3\2\2\2./\7k\2\2/\60")
        buf.write("\7p\2\2\60\61\7v\2\2\61\6\3\2\2\2\62\63\7x\2\2\63\64\7")
        buf.write("q\2\2\64\65\7k\2\2\65\66\7f\2\2\66\b\3\2\2\2\679\t\2\2")
        buf.write("\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;\n\3\2\2")
        buf.write("\2<>\t\3\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@")
        buf.write("\f\3\2\2\2AB\7*\2\2B\16\3\2\2\2CD\7+\2\2D\20\3\2\2\2E")
        buf.write("F\7}\2\2F\22\3\2\2\2GH\7\177\2\2H\24\3\2\2\2IJ\7=\2\2")
        buf.write("J\26\3\2\2\2KM\t\4\2\2LK\3\2\2\2MN\3\2\2\2NL\3\2\2\2N")
        buf.write("O\3\2\2\2OP\3\2\2\2PQ\b\f\2\2Q\30\3\2\2\2RS\t\5\2\2S\32")
        buf.write("\3\2\2\2TU\t\3\2\2U\34\3\2\2\2V[\5\31\r\2WZ\5\31\r\2X")
        buf.write("Z\5\33\16\2YW\3\2\2\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\")
        buf.write("\3\2\2\2\\\36\3\2\2\2][\3\2\2\2^`\5\33\16\2_^\3\2\2\2")
        buf.write("`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bd\3\2\2\2ca\3\2\2\2df\7")
        buf.write("\60\2\2eg\5\33\16\2fe\3\2\2\2gh\3\2\2\2hf\3\2\2\2hi\3")
        buf.write("\2\2\2i\u0082\3\2\2\2jl\5\33\16\2kj\3\2\2\2lo\3\2\2\2")
        buf.write("mk\3\2\2\2mn\3\2\2\2nv\3\2\2\2om\3\2\2\2pr\7\60\2\2qs")
        buf.write("\5\33\16\2rq\3\2\2\2st\3\2\2\2tr\3\2\2\2tu\3\2\2\2uw\3")
        buf.write("\2\2\2vp\3\2\2\2vw\3\2\2\2wx\3\2\2\2xz\7g\2\2y{\7/\2\2")
        buf.write("zy\3\2\2\2z{\3\2\2\2{}\3\2\2\2|~\5\33\16\2}|\3\2\2\2~")
        buf.write("\177\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082")
        buf.write("\3\2\2\2\u0081a\3\2\2\2\u0081m\3\2\2\2\u0082 \3\2\2\2")
        buf.write("\u0083\u0087\7)\2\2\u0084\u0088\n\6\2\2\u0085\u0086\7")
        buf.write(")\2\2\u0086\u0088\7)\2\2\u0087\u0084\3\2\2\2\u0087\u0085")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u0087\3\2\2\2\u0089")
        buf.write("\u008a\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\7)\2\2")
        buf.write("\u008c\"\3\2\2\2\u008d\u008e\13\2\2\2\u008e$\3\2\2\2\u008f")
        buf.write("\u0090\13\2\2\2\u0090&\3\2\2\2\u0091\u0092\13\2\2\2\u0092")
        buf.write("(\3\2\2\2\22\2:?NY[ahmtvz\177\u0081\u0087\u0089\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    ID = 4
    INTLIT = 5
    LB = 6
    RB = 7
    LP = 8
    RP = 9
    SEMI = 10
    WS = 11
    CIDENTIFIER = 12
    REAL = 13
    STRING = 14
    ERROR_CHAR = 15
    UNCLOSE_STRING = 16
    ILLEGAL_ESCAPE = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", "LP", "RP", 
            "SEMI", "WS", "CIDENTIFIER", "REAL", "STRING", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", 
                  "LP", "RP", "SEMI", "WS", "LETTER", "DIGIT", "CIDENTIFIER", 
                  "REAL", "STRING", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


