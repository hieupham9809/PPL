# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("\u0083\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\6\5\67\n\5\r\5\16\58\3\6\6\6<\n\6\r\6\16")
        buf.write("\6=\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\6\f")
        buf.write("K\n\f\r\f\16\fL\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3")
        buf.write("\17\7\17X\n\17\f\17\16\17[\13\17\3\20\6\20^\n\20\r\20")
        buf.write("\16\20_\3\20\3\20\6\20d\n\20\r\20\16\20e\3\20\6\20i\n")
        buf.write("\20\r\20\16\20j\3\20\3\20\6\20o\n\20\r\20\16\20p\3\20")
        buf.write("\3\20\5\20u\n\20\3\20\6\20x\n\20\r\20\16\20y\5\20|\n\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\2\2\24\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\2\33\2\35\16\37")
        buf.write("\17!\20#\21%\22\3\2\6\4\2C\\c|\3\2\62;\5\2\13\f\17\17")
        buf.write("\"\"\3\2c|\2\u008c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3")
        buf.write("\'\3\2\2\2\5,\3\2\2\2\7\60\3\2\2\2\t\66\3\2\2\2\13;\3")
        buf.write("\2\2\2\r?\3\2\2\2\17A\3\2\2\2\21C\3\2\2\2\23E\3\2\2\2")
        buf.write("\25G\3\2\2\2\27J\3\2\2\2\31P\3\2\2\2\33R\3\2\2\2\35T\3")
        buf.write("\2\2\2\37{\3\2\2\2!}\3\2\2\2#\177\3\2\2\2%\u0081\3\2\2")
        buf.write("\2\'(\7o\2\2()\7c\2\2)*\7k\2\2*+\7p\2\2+\4\3\2\2\2,-\7")
        buf.write("k\2\2-.\7p\2\2./\7v\2\2/\6\3\2\2\2\60\61\7x\2\2\61\62")
        buf.write("\7q\2\2\62\63\7k\2\2\63\64\7f\2\2\64\b\3\2\2\2\65\67\t")
        buf.write("\2\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\2")
        buf.write("9\n\3\2\2\2:<\t\3\2\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>")
        buf.write("\3\2\2\2>\f\3\2\2\2?@\7*\2\2@\16\3\2\2\2AB\7+\2\2B\20")
        buf.write("\3\2\2\2CD\7}\2\2D\22\3\2\2\2EF\7\177\2\2F\24\3\2\2\2")
        buf.write("GH\7=\2\2H\26\3\2\2\2IK\t\4\2\2JI\3\2\2\2KL\3\2\2\2LJ")
        buf.write("\3\2\2\2LM\3\2\2\2MN\3\2\2\2NO\b\f\2\2O\30\3\2\2\2PQ\t")
        buf.write("\5\2\2Q\32\3\2\2\2RS\t\3\2\2S\34\3\2\2\2TY\5\31\r\2UX")
        buf.write("\5\31\r\2VX\5\33\16\2WU\3\2\2\2WV\3\2\2\2X[\3\2\2\2YW")
        buf.write("\3\2\2\2YZ\3\2\2\2Z\36\3\2\2\2[Y\3\2\2\2\\^\5\33\16\2")
        buf.write("]\\\3\2\2\2^_\3\2\2\2_]\3\2\2\2_`\3\2\2\2`a\3\2\2\2ac")
        buf.write("\7\60\2\2bd\5\33\16\2cb\3\2\2\2de\3\2\2\2ec\3\2\2\2ef")
        buf.write("\3\2\2\2f|\3\2\2\2gi\5\33\16\2hg\3\2\2\2ij\3\2\2\2jh\3")
        buf.write("\2\2\2jk\3\2\2\2kl\3\2\2\2ln\7\60\2\2mo\5\33\16\2nm\3")
        buf.write("\2\2\2op\3\2\2\2pn\3\2\2\2pq\3\2\2\2qr\3\2\2\2rt\7g\2")
        buf.write("\2su\7/\2\2ts\3\2\2\2tu\3\2\2\2uw\3\2\2\2vx\5\33\16\2")
        buf.write("wv\3\2\2\2xy\3\2\2\2yw\3\2\2\2yz\3\2\2\2z|\3\2\2\2{]\3")
        buf.write("\2\2\2{h\3\2\2\2| \3\2\2\2}~\13\2\2\2~\"\3\2\2\2\177\u0080")
        buf.write("\13\2\2\2\u0080$\3\2\2\2\u0081\u0082\13\2\2\2\u0082&\3")
        buf.write("\2\2\2\17\28=LWY_ejpty{\3\b\2\2")
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
    ERROR_CHAR = 14
    UNCLOSE_STRING = 15
    ILLEGAL_ESCAPE = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", "LP", "RP", 
            "SEMI", "WS", "CIDENTIFIER", "REAL", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", 
                  "LP", "RP", "SEMI", "WS", "LETTER", "DIGIT", "CIDENTIFIER", 
                  "REAL", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


