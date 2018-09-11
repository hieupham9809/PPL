# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u0269\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\38\39\39\39\39\39\3:\3:")
        buf.write("\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\5:\u01ab\n:\3;\3;\5;\u01af\n;\3;\3")
        buf.write(";\7;\u01b3\n;\f;\16;\u01b6\13;\3<\3<\3<\3=\3=\3>\3>\3")
        buf.write("?\3?\3?\3@\3@\3A\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3")
        buf.write("F\3G\3G\3H\6H\u01d5\nH\rH\16H\u01d6\3I\3I\6I\u01db\nI")
        buf.write("\rI\16I\u01dc\5I\u01df\nI\3I\3I\3I\5I\u01e4\nI\3J\3J\5")
        buf.write("J\u01e8\nJ\3K\3K\3K\3K\7K\u01ee\nK\fK\16K\u01f1\13K\3")
        buf.write("K\3K\3L\3L\7L\u01f7\nL\fL\16L\u01fa\13L\3L\3L\3L\3M\7")
        buf.write("M\u0200\nM\fM\16M\u0203\13M\3M\3M\6M\u0207\nM\rM\16M\u0208")
        buf.write("\3M\6M\u020c\nM\rM\16M\u020d\3M\3M\7M\u0212\nM\fM\16M")
        buf.write("\u0215\13M\5M\u0217\nM\3N\3N\5N\u021b\nN\3N\6N\u021e\n")
        buf.write("N\rN\16N\u021f\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3U")
        buf.write("\3U\3V\3V\3V\3W\6W\u0234\nW\rW\16W\u0235\3W\3W\3X\3X\3")
        buf.write("X\3X\7X\u023e\nX\fX\16X\u0241\13X\3X\3X\3X\3X\3X\3Y\3")
        buf.write("Y\7Y\u024a\nY\fY\16Y\u024d\13Y\3Y\3Y\3Y\3Y\3Z\3Z\3Z\3")
        buf.write("Z\7Z\u0257\nZ\fZ\16Z\u025a\13Z\3Z\3Z\3[\3[\3[\3\\\3\\")
        buf.write("\7\\\u0263\n\\\f\\\16\\\u0266\13\\\3\\\3\\\4\u023f\u024b")
        buf.write("\2]\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2")
        buf.write("\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63")
        buf.write("\2\65\2\67\39\4;\5=\6?\7A\bC\tE\nG\13I\fK\rM\16O\17Q\20")
        buf.write("S\21U\22W\23Y\24[\25]\26_\27a\30c\31e\32g\33i\34k\35m")
        buf.write("\36o\37q s\2u!w\"y#{$}%\177&\u0081\'\u0083(\u0085)\u0087")
        buf.write("*\u0089+\u008b,\u008d\2\u008f-\u0091.\u0093/\u0095\60")
        buf.write("\u0097\61\u0099\2\u009b\2\u009d\62\u009f\63\u00a1\64\u00a3")
        buf.write("\65\u00a5\66\u00a7\67\u00a98\u00ab9\u00ad:\u00af;\u00b1")
        buf.write("<\u00b3=\u00b5>\u00b7?\3\2$\4\2CCcc\4\2DDdd\4\2EEee\4")
        buf.write("\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLl")
        buf.write("l\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2")
        buf.write("SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4")
        buf.write("\2ZZzz\4\2[[{{\4\2\\\\||\4\2\62;aa\3\2\62;\3\2^^\n\2$")
        buf.write("$))^^ddhhppttvv\6\2\n\f\16\17$$))\5\2\13\f\17\17\"\"\4")
        buf.write("\2\f\f\17\17\4\2\f\f$$\2\u027a\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af")
        buf.write("\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2")
        buf.write("\2\2\u00b7\3\2\2\2\3\u00b9\3\2\2\2\5\u00bb\3\2\2\2\7\u00bd")
        buf.write("\3\2\2\2\t\u00bf\3\2\2\2\13\u00c1\3\2\2\2\r\u00c3\3\2")
        buf.write("\2\2\17\u00c5\3\2\2\2\21\u00c7\3\2\2\2\23\u00c9\3\2\2")
        buf.write("\2\25\u00cb\3\2\2\2\27\u00cd\3\2\2\2\31\u00cf\3\2\2\2")
        buf.write("\33\u00d1\3\2\2\2\35\u00d3\3\2\2\2\37\u00d5\3\2\2\2!\u00d7")
        buf.write("\3\2\2\2#\u00d9\3\2\2\2%\u00db\3\2\2\2\'\u00dd\3\2\2\2")
        buf.write(")\u00df\3\2\2\2+\u00e1\3\2\2\2-\u00e3\3\2\2\2/\u00e5\3")
        buf.write("\2\2\2\61\u00e7\3\2\2\2\63\u00e9\3\2\2\2\65\u00eb\3\2")
        buf.write("\2\2\67\u00ed\3\2\2\29\u00f3\3\2\2\2;\u00fc\3\2\2\2=\u0100")
        buf.write("\3\2\2\2?\u0103\3\2\2\2A\u010a\3\2\2\2C\u010d\3\2\2\2")
        buf.write("E\u0110\3\2\2\2G\u0115\3\2\2\2I\u011a\3\2\2\2K\u0121\3")
        buf.write("\2\2\2M\u0127\3\2\2\2O\u012d\3\2\2\2Q\u0131\3\2\2\2S\u013a")
        buf.write("\3\2\2\2U\u0144\3\2\2\2W\u0148\3\2\2\2Y\u014d\3\2\2\2")
        buf.write("[\u0153\3\2\2\2]\u0159\3\2\2\2_\u015c\3\2\2\2a\u0161\3")
        buf.write("\2\2\2c\u0169\3\2\2\2e\u0171\3\2\2\2g\u0178\3\2\2\2i\u017c")
        buf.write("\3\2\2\2k\u0180\3\2\2\2m\u0183\3\2\2\2o\u0187\3\2\2\2")
        buf.write("q\u018b\3\2\2\2s\u01aa\3\2\2\2u\u01ae\3\2\2\2w\u01b7\3")
        buf.write("\2\2\2y\u01ba\3\2\2\2{\u01bc\3\2\2\2}\u01be\3\2\2\2\177")
        buf.write("\u01c1\3\2\2\2\u0081\u01c3\3\2\2\2\u0083\u01c6\3\2\2\2")
        buf.write("\u0085\u01c8\3\2\2\2\u0087\u01ca\3\2\2\2\u0089\u01cc\3")
        buf.write("\2\2\2\u008b\u01ce\3\2\2\2\u008d\u01d1\3\2\2\2\u008f\u01d4")
        buf.write("\3\2\2\2\u0091\u01e3\3\2\2\2\u0093\u01e7\3\2\2\2\u0095")
        buf.write("\u01e9\3\2\2\2\u0097\u01f4\3\2\2\2\u0099\u0216\3\2\2\2")
        buf.write("\u009b\u0218\3\2\2\2\u009d\u0221\3\2\2\2\u009f\u0223\3")
        buf.write("\2\2\2\u00a1\u0225\3\2\2\2\u00a3\u0227\3\2\2\2\u00a5\u0229")
        buf.write("\3\2\2\2\u00a7\u022b\3\2\2\2\u00a9\u022d\3\2\2\2\u00ab")
        buf.write("\u022f\3\2\2\2\u00ad\u0233\3\2\2\2\u00af\u0239\3\2\2\2")
        buf.write("\u00b1\u0247\3\2\2\2\u00b3\u0252\3\2\2\2\u00b5\u025d\3")
        buf.write("\2\2\2\u00b7\u0260\3\2\2\2\u00b9\u00ba\t\2\2\2\u00ba\4")
        buf.write("\3\2\2\2\u00bb\u00bc\t\3\2\2\u00bc\6\3\2\2\2\u00bd\u00be")
        buf.write("\t\4\2\2\u00be\b\3\2\2\2\u00bf\u00c0\t\5\2\2\u00c0\n\3")
        buf.write("\2\2\2\u00c1\u00c2\t\6\2\2\u00c2\f\3\2\2\2\u00c3\u00c4")
        buf.write("\t\7\2\2\u00c4\16\3\2\2\2\u00c5\u00c6\t\b\2\2\u00c6\20")
        buf.write("\3\2\2\2\u00c7\u00c8\t\t\2\2\u00c8\22\3\2\2\2\u00c9\u00ca")
        buf.write("\t\n\2\2\u00ca\24\3\2\2\2\u00cb\u00cc\t\13\2\2\u00cc\26")
        buf.write("\3\2\2\2\u00cd\u00ce\t\f\2\2\u00ce\30\3\2\2\2\u00cf\u00d0")
        buf.write("\t\r\2\2\u00d0\32\3\2\2\2\u00d1\u00d2\t\16\2\2\u00d2\34")
        buf.write("\3\2\2\2\u00d3\u00d4\t\17\2\2\u00d4\36\3\2\2\2\u00d5\u00d6")
        buf.write("\t\20\2\2\u00d6 \3\2\2\2\u00d7\u00d8\t\21\2\2\u00d8\"")
        buf.write("\3\2\2\2\u00d9\u00da\t\22\2\2\u00da$\3\2\2\2\u00db\u00dc")
        buf.write("\t\23\2\2\u00dc&\3\2\2\2\u00dd\u00de\t\24\2\2\u00de(\3")
        buf.write("\2\2\2\u00df\u00e0\t\25\2\2\u00e0*\3\2\2\2\u00e1\u00e2")
        buf.write("\t\26\2\2\u00e2,\3\2\2\2\u00e3\u00e4\t\27\2\2\u00e4.\3")
        buf.write("\2\2\2\u00e5\u00e6\t\30\2\2\u00e6\60\3\2\2\2\u00e7\u00e8")
        buf.write("\t\31\2\2\u00e8\62\3\2\2\2\u00e9\u00ea\t\32\2\2\u00ea")
        buf.write("\64\3\2\2\2\u00eb\u00ec\t\33\2\2\u00ec\66\3\2\2\2\u00ed")
        buf.write("\u00ee\5\5\3\2\u00ee\u00ef\5%\23\2\u00ef\u00f0\5\13\6")
        buf.write("\2\u00f0\u00f1\5\3\2\2\u00f1\u00f2\5\27\f\2\u00f28\3\2")
        buf.write("\2\2\u00f3\u00f4\5\7\4\2\u00f4\u00f5\5\37\20\2\u00f5\u00f6")
        buf.write("\5\35\17\2\u00f6\u00f7\5)\25\2\u00f7\u00f8\5\23\n\2\u00f8")
        buf.write("\u00f9\5\35\17\2\u00f9\u00fa\5+\26\2\u00fa\u00fb\5\13")
        buf.write("\6\2\u00fb:\3\2\2\2\u00fc\u00fd\5\r\7\2\u00fd\u00fe\5")
        buf.write("\37\20\2\u00fe\u00ff\5%\23\2\u00ff<\3\2\2\2\u0100\u0101")
        buf.write("\5)\25\2\u0101\u0102\5\37\20\2\u0102>\3\2\2\2\u0103\u0104")
        buf.write("\5\t\5\2\u0104\u0105\5\37\20\2\u0105\u0106\5/\30\2\u0106")
        buf.write("\u0107\5\35\17\2\u0107\u0108\5)\25\2\u0108\u0109\5\37")
        buf.write("\20\2\u0109@\3\2\2\2\u010a\u010b\5\t\5\2\u010b\u010c\5")
        buf.write("\37\20\2\u010cB\3\2\2\2\u010d\u010e\5\23\n\2\u010e\u010f")
        buf.write("\5\r\7\2\u010fD\3\2\2\2\u0110\u0111\5)\25\2\u0111\u0112")
        buf.write("\5\21\t\2\u0112\u0113\5\13\6\2\u0113\u0114\5\35\17\2\u0114")
        buf.write("F\3\2\2\2\u0115\u0116\5\13\6\2\u0116\u0117\5\31\r\2\u0117")
        buf.write("\u0118\5\'\24\2\u0118\u0119\5\13\6\2\u0119H\3\2\2\2\u011a")
        buf.write("\u011b\5%\23\2\u011b\u011c\5\13\6\2\u011c\u011d\5)\25")
        buf.write("\2\u011d\u011e\5+\26\2\u011e\u011f\5%\23\2\u011f\u0120")
        buf.write("\5\35\17\2\u0120J\3\2\2\2\u0121\u0122\5/\30\2\u0122\u0123")
        buf.write("\5\21\t\2\u0123\u0124\5\23\n\2\u0124\u0125\5\31\r\2\u0125")
        buf.write("\u0126\5\13\6\2\u0126L\3\2\2\2\u0127\u0128\5\5\3\2\u0128")
        buf.write("\u0129\5\13\6\2\u0129\u012a\5\17\b\2\u012a\u012b\5\23")
        buf.write("\n\2\u012b\u012c\5\35\17\2\u012cN\3\2\2\2\u012d\u012e")
        buf.write("\5\13\6\2\u012e\u012f\5\35\17\2\u012f\u0130\5\t\5\2\u0130")
        buf.write("P\3\2\2\2\u0131\u0132\5\r\7\2\u0132\u0133\5+\26\2\u0133")
        buf.write("\u0134\5\35\17\2\u0134\u0135\5\7\4\2\u0135\u0136\5)\25")
        buf.write("\2\u0136\u0137\5\23\n\2\u0137\u0138\5\37\20\2\u0138\u0139")
        buf.write("\5\35\17\2\u0139R\3\2\2\2\u013a\u013b\5!\21\2\u013b\u013c")
        buf.write("\5%\23\2\u013c\u013d\5\37\20\2\u013d\u013e\5\7\4\2\u013e")
        buf.write("\u013f\5\13\6\2\u013f\u0140\5\t\5\2\u0140\u0141\5+\26")
        buf.write("\2\u0141\u0142\5%\23\2\u0142\u0143\5\13\6\2\u0143T\3\2")
        buf.write("\2\2\u0144\u0145\5-\27\2\u0145\u0146\5\3\2\2\u0146\u0147")
        buf.write("\5%\23\2\u0147V\3\2\2\2\u0148\u0149\5)\25\2\u0149\u014a")
        buf.write("\5%\23\2\u014a\u014b\5+\26\2\u014b\u014c\5\13\6\2\u014c")
        buf.write("X\3\2\2\2\u014d\u014e\5\r\7\2\u014e\u014f\5\3\2\2\u014f")
        buf.write("\u0150\5\31\r\2\u0150\u0151\5\'\24\2\u0151\u0152\5\13")
        buf.write("\6\2\u0152Z\3\2\2\2\u0153\u0154\5\3\2\2\u0154\u0155\5")
        buf.write("%\23\2\u0155\u0156\5%\23\2\u0156\u0157\5\3\2\2\u0157\u0158")
        buf.write("\5\63\32\2\u0158\\\3\2\2\2\u0159\u015a\5\37\20\2\u015a")
        buf.write("\u015b\5\r\7\2\u015b^\3\2\2\2\u015c\u015d\5%\23\2\u015d")
        buf.write("\u015e\5\13\6\2\u015e\u015f\5\3\2\2\u015f\u0160\5\31\r")
        buf.write("\2\u0160`\3\2\2\2\u0161\u0162\5\5\3\2\u0162\u0163\5\37")
        buf.write("\20\2\u0163\u0164\5\37\20\2\u0164\u0165\5\31\r\2\u0165")
        buf.write("\u0166\5\13\6\2\u0166\u0167\5\3\2\2\u0167\u0168\5\35\17")
        buf.write("\2\u0168b\3\2\2\2\u0169\u016a\5\23\n\2\u016a\u016b\5\35")
        buf.write("\17\2\u016b\u016c\5)\25\2\u016c\u016d\5\13\6\2\u016d\u016e")
        buf.write("\5\17\b\2\u016e\u016f\5\13\6\2\u016f\u0170\5%\23\2\u0170")
        buf.write("d\3\2\2\2\u0171\u0172\5\'\24\2\u0172\u0173\5)\25\2\u0173")
        buf.write("\u0174\5%\23\2\u0174\u0175\5\23\n\2\u0175\u0176\5\35\17")
        buf.write("\2\u0176\u0177\5\17\b\2\u0177f\3\2\2\2\u0178\u0179\5\35")
        buf.write("\17\2\u0179\u017a\5\37\20\2\u017a\u017b\5)\25\2\u017b")
        buf.write("h\3\2\2\2\u017c\u017d\5\3\2\2\u017d\u017e\5\35\17\2\u017e")
        buf.write("\u017f\5\t\5\2\u017fj\3\2\2\2\u0180\u0181\5\37\20\2\u0181")
        buf.write("\u0182\5%\23\2\u0182l\3\2\2\2\u0183\u0184\5\t\5\2\u0184")
        buf.write("\u0185\5\23\n\2\u0185\u0186\5-\27\2\u0186n\3\2\2\2\u0187")
        buf.write("\u0188\5\33\16\2\u0188\u0189\5\37\20\2\u0189\u018a\5\t")
        buf.write("\5\2\u018ap\3\2\2\2\u018b\u018c\5/\30\2\u018c\u018d\5")
        buf.write("\23\n\2\u018d\u018e\5)\25\2\u018e\u018f\5\21\t\2\u018f")
        buf.write("r\3\2\2\2\u0190\u01ab\5\3\2\2\u0191\u01ab\5\5\3\2\u0192")
        buf.write("\u01ab\5\7\4\2\u0193\u01ab\5\t\5\2\u0194\u01ab\5\13\6")
        buf.write("\2\u0195\u01ab\5\r\7\2\u0196\u01ab\5\17\b\2\u0197\u01ab")
        buf.write("\5\21\t\2\u0198\u01ab\5\23\n\2\u0199\u01ab\5\25\13\2\u019a")
        buf.write("\u01ab\5\27\f\2\u019b\u01ab\5\31\r\2\u019c\u01ab\5\33")
        buf.write("\16\2\u019d\u01ab\5\35\17\2\u019e\u01ab\5\37\20\2\u019f")
        buf.write("\u01ab\5!\21\2\u01a0\u01ab\5#\22\2\u01a1\u01ab\5%\23\2")
        buf.write("\u01a2\u01ab\5\'\24\2\u01a3\u01ab\5)\25\2\u01a4\u01ab")
        buf.write("\5+\26\2\u01a5\u01ab\5-\27\2\u01a6\u01ab\5/\30\2\u01a7")
        buf.write("\u01ab\5\61\31\2\u01a8\u01ab\5\63\32\2\u01a9\u01ab\5\65")
        buf.write("\33\2\u01aa\u0190\3\2\2\2\u01aa\u0191\3\2\2\2\u01aa\u0192")
        buf.write("\3\2\2\2\u01aa\u0193\3\2\2\2\u01aa\u0194\3\2\2\2\u01aa")
        buf.write("\u0195\3\2\2\2\u01aa\u0196\3\2\2\2\u01aa\u0197\3\2\2\2")
        buf.write("\u01aa\u0198\3\2\2\2\u01aa\u0199\3\2\2\2\u01aa\u019a\3")
        buf.write("\2\2\2\u01aa\u019b\3\2\2\2\u01aa\u019c\3\2\2\2\u01aa\u019d")
        buf.write("\3\2\2\2\u01aa\u019e\3\2\2\2\u01aa\u019f\3\2\2\2\u01aa")
        buf.write("\u01a0\3\2\2\2\u01aa\u01a1\3\2\2\2\u01aa\u01a2\3\2\2\2")
        buf.write("\u01aa\u01a3\3\2\2\2\u01aa\u01a4\3\2\2\2\u01aa\u01a5\3")
        buf.write("\2\2\2\u01aa\u01a6\3\2\2\2\u01aa\u01a7\3\2\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2\u01aa\u01a9\3\2\2\2\u01abt\3\2\2\2\u01ac\u01af")
        buf.write("\5s:\2\u01ad\u01af\7a\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01ad")
        buf.write("\3\2\2\2\u01af\u01b4\3\2\2\2\u01b0\u01b3\5s:\2\u01b1\u01b3")
        buf.write("\t\34\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3")
        buf.write("\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5v\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01b8\7<\2\2")
        buf.write("\u01b8\u01b9\7?\2\2\u01b9x\3\2\2\2\u01ba\u01bb\7-\2\2")
        buf.write("\u01bbz\3\2\2\2\u01bc\u01bd\7,\2\2\u01bd|\3\2\2\2\u01be")
        buf.write("\u01bf\7>\2\2\u01bf\u01c0\7@\2\2\u01c0~\3\2\2\2\u01c1")
        buf.write("\u01c2\7>\2\2\u01c2\u0080\3\2\2\2\u01c3\u01c4\7>\2\2\u01c4")
        buf.write("\u01c5\7?\2\2\u01c5\u0082\3\2\2\2\u01c6\u01c7\7/\2\2\u01c7")
        buf.write("\u0084\3\2\2\2\u01c8\u01c9\7\61\2\2\u01c9\u0086\3\2\2")
        buf.write("\2\u01ca\u01cb\7?\2\2\u01cb\u0088\3\2\2\2\u01cc\u01cd")
        buf.write("\7@\2\2\u01cd\u008a\3\2\2\2\u01ce\u01cf\7@\2\2\u01cf\u01d0")
        buf.write("\7?\2\2\u01d0\u008c\3\2\2\2\u01d1\u01d2\t\35\2\2\u01d2")
        buf.write("\u008e\3\2\2\2\u01d3\u01d5\5\u008dG\2\u01d4\u01d3\3\2")
        buf.write("\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7\u0090\3\2\2\2\u01d8\u01df\5\u0099M\2\u01d9")
        buf.write("\u01db\5\u008dG\2\u01da\u01d9\3\2\2\2\u01db\u01dc\3\2")
        buf.write("\2\2\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df")
        buf.write("\3\2\2\2\u01de\u01d8\3\2\2\2\u01de\u01da\3\2\2\2\u01df")
        buf.write("\u01e0\3\2\2\2\u01e0\u01e1\5\u009bN\2\u01e1\u01e4\3\2")
        buf.write("\2\2\u01e2\u01e4\5\u0099M\2\u01e3\u01de\3\2\2\2\u01e3")
        buf.write("\u01e2\3\2\2\2\u01e4\u0092\3\2\2\2\u01e5\u01e8\5W,\2\u01e6")
        buf.write("\u01e8\5Y-\2\u01e7\u01e5\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8")
        buf.write("\u0094\3\2\2\2\u01e9\u01ef\7$\2\2\u01ea\u01ee\n\36\2\2")
        buf.write("\u01eb\u01ec\7^\2\2\u01ec\u01ee\n\37\2\2\u01ed\u01ea\3")
        buf.write("\2\2\2\u01ed\u01eb\3\2\2\2\u01ee\u01f1\3\2\2\2\u01ef\u01ed")
        buf.write("\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f2\3\2\2\2\u01f1")
        buf.write("\u01ef\3\2\2\2\u01f2\u01f3\bK\2\2\u01f3\u0096\3\2\2\2")
        buf.write("\u01f4\u01f8\7$\2\2\u01f5\u01f7\n \2\2\u01f6\u01f5\3\2")
        buf.write("\2\2\u01f7\u01fa\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9")
        buf.write("\3\2\2\2\u01f9\u01fb\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fb")
        buf.write("\u01fc\7$\2\2\u01fc\u01fd\bL\3\2\u01fd\u0098\3\2\2\2\u01fe")
        buf.write("\u0200\5\u008dG\2\u01ff\u01fe\3\2\2\2\u0200\u0203\3\2")
        buf.write("\2\2\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0204")
        buf.write("\3\2\2\2\u0203\u0201\3\2\2\2\u0204\u0206\7\60\2\2\u0205")
        buf.write("\u0207\5\u008dG\2\u0206\u0205\3\2\2\2\u0207\u0208\3\2")
        buf.write("\2\2\u0208\u0206\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u0217")
        buf.write("\3\2\2\2\u020a\u020c\5\u008dG\2\u020b\u020a\3\2\2\2\u020c")
        buf.write("\u020d\3\2\2\2\u020d\u020b\3\2\2\2\u020d\u020e\3\2\2\2")
        buf.write("\u020e\u020f\3\2\2\2\u020f\u0213\7\60\2\2\u0210\u0212")
        buf.write("\5\u008dG\2\u0211\u0210\3\2\2\2\u0212\u0215\3\2\2\2\u0213")
        buf.write("\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0217\3\2\2\2")
        buf.write("\u0215\u0213\3\2\2\2\u0216\u0201\3\2\2\2\u0216\u020b\3")
        buf.write("\2\2\2\u0217\u009a\3\2\2\2\u0218\u021a\5\13\6\2\u0219")
        buf.write("\u021b\7/\2\2\u021a\u0219\3\2\2\2\u021a\u021b\3\2\2\2")
        buf.write("\u021b\u021d\3\2\2\2\u021c\u021e\5\u008dG\2\u021d\u021c")
        buf.write("\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u021d\3\2\2\2\u021f")
        buf.write("\u0220\3\2\2\2\u0220\u009c\3\2\2\2\u0221\u0222\7*\2\2")
        buf.write("\u0222\u009e\3\2\2\2\u0223\u0224\7+\2\2\u0224\u00a0\3")
        buf.write("\2\2\2\u0225\u0226\7=\2\2\u0226\u00a2\3\2\2\2\u0227\u0228")
        buf.write("\7.\2\2\u0228\u00a4\3\2\2\2\u0229\u022a\7]\2\2\u022a\u00a6")
        buf.write("\3\2\2\2\u022b\u022c\7_\2\2\u022c\u00a8\3\2\2\2\u022d")
        buf.write("\u022e\7<\2\2\u022e\u00aa\3\2\2\2\u022f\u0230\7\60\2\2")
        buf.write("\u0230\u0231\7\60\2\2\u0231\u00ac\3\2\2\2\u0232\u0234")
        buf.write("\t!\2\2\u0233\u0232\3\2\2\2\u0234\u0235\3\2\2\2\u0235")
        buf.write("\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0237\3\2\2\2")
        buf.write("\u0237\u0238\bW\4\2\u0238\u00ae\3\2\2\2\u0239\u023a\7")
        buf.write("*\2\2\u023a\u023b\7,\2\2\u023b\u023f\3\2\2\2\u023c\u023e")
        buf.write("\13\2\2\2\u023d\u023c\3\2\2\2\u023e\u0241\3\2\2\2\u023f")
        buf.write("\u0240\3\2\2\2\u023f\u023d\3\2\2\2\u0240\u0242\3\2\2\2")
        buf.write("\u0241\u023f\3\2\2\2\u0242\u0243\7,\2\2\u0243\u0244\7")
        buf.write("+\2\2\u0244\u0245\3\2\2\2\u0245\u0246\bX\4\2\u0246\u00b0")
        buf.write("\3\2\2\2\u0247\u024b\7}\2\2\u0248\u024a\13\2\2\2\u0249")
        buf.write("\u0248\3\2\2\2\u024a\u024d\3\2\2\2\u024b\u024c\3\2\2\2")
        buf.write("\u024b\u0249\3\2\2\2\u024c\u024e\3\2\2\2\u024d\u024b\3")
        buf.write("\2\2\2\u024e\u024f\7\177\2\2\u024f\u0250\3\2\2\2\u0250")
        buf.write("\u0251\bY\4\2\u0251\u00b2\3\2\2\2\u0252\u0253\7\61\2\2")
        buf.write("\u0253\u0254\7\61\2\2\u0254\u0258\3\2\2\2\u0255\u0257")
        buf.write("\n\"\2\2\u0256\u0255\3\2\2\2\u0257\u025a\3\2\2\2\u0258")
        buf.write("\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u025b\3\2\2\2")
        buf.write("\u025a\u0258\3\2\2\2\u025b\u025c\bZ\4\2\u025c\u00b4\3")
        buf.write("\2\2\2\u025d\u025e\13\2\2\2\u025e\u025f\b[\5\2\u025f\u00b6")
        buf.write("\3\2\2\2\u0260\u0264\7$\2\2\u0261\u0263\n#\2\2\u0262\u0261")
        buf.write("\3\2\2\2\u0263\u0266\3\2\2\2\u0264\u0262\3\2\2\2\u0264")
        buf.write("\u0265\3\2\2\2\u0265\u0267\3\2\2\2\u0266\u0264\3\2\2\2")
        buf.write("\u0267\u0268\b\\\6\2\u0268\u00b8\3\2\2\2\33\2\u01aa\u01ae")
        buf.write("\u01b2\u01b4\u01d6\u01dc\u01de\u01e3\u01e7\u01ed\u01ef")
        buf.write("\u01f8\u0201\u0208\u020d\u0213\u0216\u021a\u021f\u0235")
        buf.write("\u023f\u024b\u0258\u0264\7\3K\2\3L\3\b\2\2\3[\4\3\\\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    FOR = 3
    TO = 4
    DOWNTO = 5
    DO = 6
    IF = 7
    THEN = 8
    ELSE = 9
    RETURNS = 10
    WHILE = 11
    BEGIN = 12
    END = 13
    FUNCTION = 14
    PROCEDURE = 15
    VAR = 16
    TRUE = 17
    FALSE = 18
    ARRAY = 19
    OF = 20
    REAL = 21
    BOOLEAN = 22
    INTEGER = 23
    STRING = 24
    NOT = 25
    AND = 26
    OR = 27
    DIV = 28
    MOD = 29
    WITH = 30
    ID = 31
    ASSIGOP = 32
    ADDOP = 33
    MULOP = 34
    NEQOP = 35
    LTOP = 36
    LTEOP = 37
    SUBOP = 38
    DIVOP = 39
    EQOP = 40
    GTOP = 41
    GTEOP = 42
    INTLIT = 43
    REALIT = 44
    BOOLIT = 45
    ILLEGAL_ESCAPE = 46
    STRLIT = 47
    LB = 48
    RB = 49
    SEMI = 50
    COMMA = 51
    LSB = 52
    RSB = 53
    COLON = 54
    DDOT = 55
    WS = 56
    BLOCKCOM_B = 57
    BLOCKCOM_P = 58
    LINECOM = 59
    ERROR_TOKEN = 60
    UNCLOSE_STRING = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", "'='", 
            "'>'", "'>='", "'('", "')'", "';'", "','", "'['", "']'", "':'", 
            "'..'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
            "ELSE", "RETURNS", "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
            "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
            "STRING", "NOT", "AND", "OR", "DIV", "MOD", "WITH", "ID", "ASSIGOP", 
            "ADDOP", "MULOP", "NEQOP", "LTOP", "LTEOP", "SUBOP", "DIVOP", 
            "EQOP", "GTOP", "GTEOP", "INTLIT", "REALIT", "BOOLIT", "ILLEGAL_ESCAPE", 
            "STRLIT", "LB", "RB", "SEMI", "COMMA", "LSB", "RSB", "COLON", 
            "DDOT", "WS", "BLOCKCOM_B", "BLOCKCOM_P", "LINECOM", "ERROR_TOKEN", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "BREAK", "CONTINUE", "FOR", "TO", 
                  "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURNS", "WHILE", 
                  "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", 
                  "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "WITH", "IDCHAR", 
                  "ID", "ASSIGOP", "ADDOP", "MULOP", "NEQOP", "LTOP", "LTEOP", 
                  "SUBOP", "DIVOP", "EQOP", "GTOP", "GTEOP", "DIGIT", "INTLIT", 
                  "REALIT", "BOOLIT", "ILLEGAL_ESCAPE", "STRLIT", "NUM_HAS_P", 
                  "EXPN", "LB", "RB", "SEMI", "COMMA", "LSB", "RSB", "COLON", 
                  "DDOT", "WS", "BLOCKCOM_B", "BLOCKCOM_P", "LINECOM", "ERROR_TOKEN", 
                  "UNCLOSE_STRING" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[73] = self.ILLEGAL_ESCAPE_action 
            actions[74] = self.STRLIT_action 
            actions[89] = self.ERROR_TOKEN_action 
            actions[90] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                                                        whole_str = self.text[1:-1] 
                                                        out_str = ""
                                                        legal = ['b','t','n','f','r','"','\'','\\']
                                                        for i in range(len(whole_str)):
                                                            if whole_str[i] == '\\':
                                                                if not whole_str[i+1] in legal:
                                                                    out_str = whole_str[0:i+2]
                                                                    break
                                                             

                                                        raise IllegalEscape(out_str)         
                                                    
     

    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                                        self.text = self.text[1:-1]
                                    
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                            raise ErrorToken(self.text)    
                        
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                            self.text = self.text[1:]    
                            raise UncloseString(self.text)    
                        
     


