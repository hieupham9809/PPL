# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("^\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\6\4\36\n\4\r\4\16\4\37\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\7\7\7+\n\7\f\7\16\7.\13\7\3\b\7\b\61\n\b\f\b\16")
        buf.write("\b\64\13\b\3\b\3\b\6\b8\n\b\r\b\16\b9\3\b\7\b=\n\b\f\b")
        buf.write("\16\b@\13\b\3\b\3\b\6\bD\n\b\r\b\16\bE\5\bH\n\b\3\b\3")
        buf.write("\b\5\bL\n\b\3\b\6\bO\n\b\r\b\16\bP\5\bS\n\b\3\t\3\t\3")
        buf.write("\t\3\t\6\tY\n\t\r\t\16\tZ\3\t\3\t\2\2\n\3\3\5\4\7\5\t")
        buf.write("\2\13\2\r\6\17\7\21\b\3\2\6\5\2\13\f\17\17\"\"\3\2c|\3")
        buf.write("\2\62;\3\2))\2h\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3\2\2\2\5\27")
        buf.write("\3\2\2\2\7\35\3\2\2\2\t#\3\2\2\2\13%\3\2\2\2\r\'\3\2\2")
        buf.write("\2\17R\3\2\2\2\21T\3\2\2\2\23\24\7k\2\2\24\25\7p\2\2\25")
        buf.write("\26\7v\2\2\26\4\3\2\2\2\27\30\7x\2\2\30\31\7q\2\2\31\32")
        buf.write("\7k\2\2\32\33\7f\2\2\33\6\3\2\2\2\34\36\t\2\2\2\35\34")
        buf.write("\3\2\2\2\36\37\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 !\3\2")
        buf.write("\2\2!\"\b\4\2\2\"\b\3\2\2\2#$\t\3\2\2$\n\3\2\2\2%&\t\4")
        buf.write("\2\2&\f\3\2\2\2\',\5\t\5\2(+\5\t\5\2)+\5\13\6\2*(\3\2")
        buf.write("\2\2*)\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3\2\2\2-\16\3\2\2")
        buf.write("\2.,\3\2\2\2/\61\5\13\6\2\60/\3\2\2\2\61\64\3\2\2\2\62")
        buf.write("\60\3\2\2\2\62\63\3\2\2\2\63\65\3\2\2\2\64\62\3\2\2\2")
        buf.write("\65\67\7\60\2\2\668\5\13\6\2\67\66\3\2\2\289\3\2\2\29")
        buf.write("\67\3\2\2\29:\3\2\2\2:S\3\2\2\2;=\5\13\6\2<;\3\2\2\2=")
        buf.write("@\3\2\2\2><\3\2\2\2>?\3\2\2\2?G\3\2\2\2@>\3\2\2\2AC\7")
        buf.write("\60\2\2BD\5\13\6\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2")
        buf.write("\2\2FH\3\2\2\2GA\3\2\2\2GH\3\2\2\2HI\3\2\2\2IK\7g\2\2")
        buf.write("JL\7/\2\2KJ\3\2\2\2KL\3\2\2\2LN\3\2\2\2MO\5\13\6\2NM\3")
        buf.write("\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QS\3\2\2\2R\62\3\2")
        buf.write("\2\2R>\3\2\2\2S\20\3\2\2\2TX\7)\2\2UY\n\5\2\2VW\7)\2\2")
        buf.write("WY\7)\2\2XU\3\2\2\2XV\3\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z[\3")
        buf.write("\2\2\2[\\\3\2\2\2\\]\7)\2\2]\22\3\2\2\2\20\2\37*,\629")
        buf.write(">EGKPRXZ\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTTYPE = 1
    VOIDTYPE = 2
    WS = 3
    CIDENTIFIER = 4
    REAL = 5
    STRING = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'void'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "WS", "CIDENTIFIER", "REAL", "STRING" ]

    ruleNames = [ "INTTYPE", "VOIDTYPE", "WS", "LETTER", "DIGIT", "CIDENTIFIER", 
                  "REAL", "STRING" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


