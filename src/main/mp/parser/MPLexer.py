# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u024f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3")
        buf.write("\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3")
        buf.write("#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3")
        buf.write(",\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\38\38\38\38\39\39\39\39\39\39\39\39\39\39\39\39\39\3")
        buf.write("9\39\39\39\39\39\39\39\39\39\39\39\39\59\u01a0\n9\3:\3")
        buf.write(":\5:\u01a4\n:\3:\3:\7:\u01a8\n:\f:\16:\u01ab\13:\3;\3")
        buf.write(";\3<\3<\3=\3=\3=\3>\3>\3?\3?\3?\3@\3@\3A\3A\3B\3B\3C\3")
        buf.write("C\3D\3D\3D\3E\3E\3F\6F\u01c7\nF\rF\16F\u01c8\3G\3G\6G")
        buf.write("\u01cd\nG\rG\16G\u01ce\5G\u01d1\nG\3G\3G\3G\5G\u01d6\n")
        buf.write("G\3H\3H\5H\u01da\nH\3I\3I\7I\u01de\nI\fI\16I\u01e1\13")
        buf.write("I\3I\3I\3I\3J\7J\u01e7\nJ\fJ\16J\u01ea\13J\3J\3J\6J\u01ee")
        buf.write("\nJ\rJ\16J\u01ef\3J\6J\u01f3\nJ\rJ\16J\u01f4\3J\3J\7J")
        buf.write("\u01f9\nJ\fJ\16J\u01fc\13J\5J\u01fe\nJ\3K\3K\5K\u0202")
        buf.write("\nK\3K\6K\u0205\nK\rK\16K\u0206\3L\3L\3M\3M\3N\3N\3O\3")
        buf.write("O\3P\3P\3Q\3Q\3R\3R\3S\3S\3S\3T\6T\u021b\nT\rT\16T\u021c")
        buf.write("\3T\3T\3U\3U\3U\3U\7U\u0225\nU\fU\16U\u0228\13U\3U\3U")
        buf.write("\3U\3U\3U\3V\3V\7V\u0231\nV\fV\16V\u0234\13V\3V\3V\3V")
        buf.write("\3V\3W\3W\3W\3W\7W\u023e\nW\fW\16W\u0241\13W\3W\3W\3X")
        buf.write("\3X\3Y\3Y\7Y\u0249\nY\fY\16Y\u024c\13Y\3Y\3Y\4\u0226\u0232")
        buf.write("\2Z\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2")
        buf.write("\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63")
        buf.write("\2\65\2\67\39\4;\5=\6?\7A\bC\tE\nG\13I\fK\rM\16O\17Q\20")
        buf.write("S\21U\22W\23Y\24[\25]\26_\27a\30c\31e\32g\33i\34k\35m")
        buf.write("\36o\37q\2s u!w\"y#{$}%\177&\u0081\'\u0083(\u0085)\u0087")
        buf.write("*\u0089\2\u008b+\u008d,\u008f-\u0091.\u0093\2\u0095\2")
        buf.write("\u0097/\u0099\60\u009b\61\u009d\62\u009f\63\u00a1\64\u00a3")
        buf.write("\65\u00a5\66\u00a7\67\u00a98\u00ab9\u00ad:\u00af;\u00b1")
        buf.write("<\3\2\"\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HH")
        buf.write("hh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2")
        buf.write("OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4")
        buf.write("\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\")
        buf.write("||\4\2\62;aa\3\2\62;\4\2\n\f\16\17\5\2\13\f\17\17\"\"")
        buf.write("\4\2\f\f\17\17\3\2$$\2\u025e\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2")
        buf.write("w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2")
        buf.write("\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9")
        buf.write("\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2")
        buf.write("\2\2\u00b1\3\2\2\2\3\u00b3\3\2\2\2\5\u00b5\3\2\2\2\7\u00b7")
        buf.write("\3\2\2\2\t\u00b9\3\2\2\2\13\u00bb\3\2\2\2\r\u00bd\3\2")
        buf.write("\2\2\17\u00bf\3\2\2\2\21\u00c1\3\2\2\2\23\u00c3\3\2\2")
        buf.write("\2\25\u00c5\3\2\2\2\27\u00c7\3\2\2\2\31\u00c9\3\2\2\2")
        buf.write("\33\u00cb\3\2\2\2\35\u00cd\3\2\2\2\37\u00cf\3\2\2\2!\u00d1")
        buf.write("\3\2\2\2#\u00d3\3\2\2\2%\u00d5\3\2\2\2\'\u00d7\3\2\2\2")
        buf.write(")\u00d9\3\2\2\2+\u00db\3\2\2\2-\u00dd\3\2\2\2/\u00df\3")
        buf.write("\2\2\2\61\u00e1\3\2\2\2\63\u00e3\3\2\2\2\65\u00e5\3\2")
        buf.write("\2\2\67\u00e7\3\2\2\29\u00ed\3\2\2\2;\u00f6\3\2\2\2=\u00fa")
        buf.write("\3\2\2\2?\u00fd\3\2\2\2A\u0104\3\2\2\2C\u0107\3\2\2\2")
        buf.write("E\u010a\3\2\2\2G\u010f\3\2\2\2I\u0114\3\2\2\2K\u011b\3")
        buf.write("\2\2\2M\u0121\3\2\2\2O\u0127\3\2\2\2Q\u012b\3\2\2\2S\u0134")
        buf.write("\3\2\2\2U\u013e\3\2\2\2W\u0142\3\2\2\2Y\u0147\3\2\2\2")
        buf.write("[\u014d\3\2\2\2]\u0153\3\2\2\2_\u0156\3\2\2\2a\u015b\3")
        buf.write("\2\2\2c\u0163\3\2\2\2e\u016b\3\2\2\2g\u0172\3\2\2\2i\u0176")
        buf.write("\3\2\2\2k\u017a\3\2\2\2m\u017d\3\2\2\2o\u0181\3\2\2\2")
        buf.write("q\u019f\3\2\2\2s\u01a3\3\2\2\2u\u01ac\3\2\2\2w\u01ae\3")
        buf.write("\2\2\2y\u01b0\3\2\2\2{\u01b3\3\2\2\2}\u01b5\3\2\2\2\177")
        buf.write("\u01b8\3\2\2\2\u0081\u01ba\3\2\2\2\u0083\u01bc\3\2\2\2")
        buf.write("\u0085\u01be\3\2\2\2\u0087\u01c0\3\2\2\2\u0089\u01c3\3")
        buf.write("\2\2\2\u008b\u01c6\3\2\2\2\u008d\u01d5\3\2\2\2\u008f\u01d9")
        buf.write("\3\2\2\2\u0091\u01db\3\2\2\2\u0093\u01fd\3\2\2\2\u0095")
        buf.write("\u01ff\3\2\2\2\u0097\u0208\3\2\2\2\u0099\u020a\3\2\2\2")
        buf.write("\u009b\u020c\3\2\2\2\u009d\u020e\3\2\2\2\u009f\u0210\3")
        buf.write("\2\2\2\u00a1\u0212\3\2\2\2\u00a3\u0214\3\2\2\2\u00a5\u0216")
        buf.write("\3\2\2\2\u00a7\u021a\3\2\2\2\u00a9\u0220\3\2\2\2\u00ab")
        buf.write("\u022e\3\2\2\2\u00ad\u0239\3\2\2\2\u00af\u0244\3\2\2\2")
        buf.write("\u00b1\u0246\3\2\2\2\u00b3\u00b4\t\2\2\2\u00b4\4\3\2\2")
        buf.write("\2\u00b5\u00b6\t\3\2\2\u00b6\6\3\2\2\2\u00b7\u00b8\t\4")
        buf.write("\2\2\u00b8\b\3\2\2\2\u00b9\u00ba\t\5\2\2\u00ba\n\3\2\2")
        buf.write("\2\u00bb\u00bc\t\6\2\2\u00bc\f\3\2\2\2\u00bd\u00be\t\7")
        buf.write("\2\2\u00be\16\3\2\2\2\u00bf\u00c0\t\b\2\2\u00c0\20\3\2")
        buf.write("\2\2\u00c1\u00c2\t\t\2\2\u00c2\22\3\2\2\2\u00c3\u00c4")
        buf.write("\t\n\2\2\u00c4\24\3\2\2\2\u00c5\u00c6\t\13\2\2\u00c6\26")
        buf.write("\3\2\2\2\u00c7\u00c8\t\f\2\2\u00c8\30\3\2\2\2\u00c9\u00ca")
        buf.write("\t\r\2\2\u00ca\32\3\2\2\2\u00cb\u00cc\t\16\2\2\u00cc\34")
        buf.write("\3\2\2\2\u00cd\u00ce\t\17\2\2\u00ce\36\3\2\2\2\u00cf\u00d0")
        buf.write("\t\20\2\2\u00d0 \3\2\2\2\u00d1\u00d2\t\21\2\2\u00d2\"")
        buf.write("\3\2\2\2\u00d3\u00d4\t\22\2\2\u00d4$\3\2\2\2\u00d5\u00d6")
        buf.write("\t\23\2\2\u00d6&\3\2\2\2\u00d7\u00d8\t\24\2\2\u00d8(\3")
        buf.write("\2\2\2\u00d9\u00da\t\25\2\2\u00da*\3\2\2\2\u00db\u00dc")
        buf.write("\t\26\2\2\u00dc,\3\2\2\2\u00dd\u00de\t\27\2\2\u00de.\3")
        buf.write("\2\2\2\u00df\u00e0\t\30\2\2\u00e0\60\3\2\2\2\u00e1\u00e2")
        buf.write("\t\31\2\2\u00e2\62\3\2\2\2\u00e3\u00e4\t\32\2\2\u00e4")
        buf.write("\64\3\2\2\2\u00e5\u00e6\t\33\2\2\u00e6\66\3\2\2\2\u00e7")
        buf.write("\u00e8\5\5\3\2\u00e8\u00e9\5%\23\2\u00e9\u00ea\5\13\6")
        buf.write("\2\u00ea\u00eb\5\3\2\2\u00eb\u00ec\5\27\f\2\u00ec8\3\2")
        buf.write("\2\2\u00ed\u00ee\5\7\4\2\u00ee\u00ef\5\37\20\2\u00ef\u00f0")
        buf.write("\5\35\17\2\u00f0\u00f1\5)\25\2\u00f1\u00f2\5\23\n\2\u00f2")
        buf.write("\u00f3\5\35\17\2\u00f3\u00f4\5+\26\2\u00f4\u00f5\5\13")
        buf.write("\6\2\u00f5:\3\2\2\2\u00f6\u00f7\5\r\7\2\u00f7\u00f8\5")
        buf.write("\37\20\2\u00f8\u00f9\5%\23\2\u00f9<\3\2\2\2\u00fa\u00fb")
        buf.write("\5)\25\2\u00fb\u00fc\5\37\20\2\u00fc>\3\2\2\2\u00fd\u00fe")
        buf.write("\5\t\5\2\u00fe\u00ff\5\37\20\2\u00ff\u0100\5/\30\2\u0100")
        buf.write("\u0101\5\35\17\2\u0101\u0102\5)\25\2\u0102\u0103\5\37")
        buf.write("\20\2\u0103@\3\2\2\2\u0104\u0105\5\t\5\2\u0105\u0106\5")
        buf.write("\37\20\2\u0106B\3\2\2\2\u0107\u0108\5\23\n\2\u0108\u0109")
        buf.write("\5\r\7\2\u0109D\3\2\2\2\u010a\u010b\5)\25\2\u010b\u010c")
        buf.write("\5\21\t\2\u010c\u010d\5\13\6\2\u010d\u010e\5\35\17\2\u010e")
        buf.write("F\3\2\2\2\u010f\u0110\5\13\6\2\u0110\u0111\5\31\r\2\u0111")
        buf.write("\u0112\5\'\24\2\u0112\u0113\5\13\6\2\u0113H\3\2\2\2\u0114")
        buf.write("\u0115\5%\23\2\u0115\u0116\5\13\6\2\u0116\u0117\5)\25")
        buf.write("\2\u0117\u0118\5+\26\2\u0118\u0119\5%\23\2\u0119\u011a")
        buf.write("\5\35\17\2\u011aJ\3\2\2\2\u011b\u011c\5/\30\2\u011c\u011d")
        buf.write("\5\21\t\2\u011d\u011e\5\23\n\2\u011e\u011f\5\31\r\2\u011f")
        buf.write("\u0120\5\13\6\2\u0120L\3\2\2\2\u0121\u0122\5\5\3\2\u0122")
        buf.write("\u0123\5\13\6\2\u0123\u0124\5\17\b\2\u0124\u0125\5\23")
        buf.write("\n\2\u0125\u0126\5\35\17\2\u0126N\3\2\2\2\u0127\u0128")
        buf.write("\5\13\6\2\u0128\u0129\5\35\17\2\u0129\u012a\5\t\5\2\u012a")
        buf.write("P\3\2\2\2\u012b\u012c\5\r\7\2\u012c\u012d\5+\26\2\u012d")
        buf.write("\u012e\5\35\17\2\u012e\u012f\5\7\4\2\u012f\u0130\5)\25")
        buf.write("\2\u0130\u0131\5\23\n\2\u0131\u0132\5\37\20\2\u0132\u0133")
        buf.write("\5\35\17\2\u0133R\3\2\2\2\u0134\u0135\5!\21\2\u0135\u0136")
        buf.write("\5%\23\2\u0136\u0137\5\37\20\2\u0137\u0138\5\7\4\2\u0138")
        buf.write("\u0139\5\13\6\2\u0139\u013a\5\t\5\2\u013a\u013b\5+\26")
        buf.write("\2\u013b\u013c\5%\23\2\u013c\u013d\5\13\6\2\u013dT\3\2")
        buf.write("\2\2\u013e\u013f\5-\27\2\u013f\u0140\5\3\2\2\u0140\u0141")
        buf.write("\5%\23\2\u0141V\3\2\2\2\u0142\u0143\5)\25\2\u0143\u0144")
        buf.write("\5%\23\2\u0144\u0145\5+\26\2\u0145\u0146\5\13\6\2\u0146")
        buf.write("X\3\2\2\2\u0147\u0148\5\r\7\2\u0148\u0149\5\3\2\2\u0149")
        buf.write("\u014a\5\31\r\2\u014a\u014b\5\'\24\2\u014b\u014c\5\13")
        buf.write("\6\2\u014cZ\3\2\2\2\u014d\u014e\5\3\2\2\u014e\u014f\5")
        buf.write("%\23\2\u014f\u0150\5%\23\2\u0150\u0151\5\3\2\2\u0151\u0152")
        buf.write("\5\63\32\2\u0152\\\3\2\2\2\u0153\u0154\5\37\20\2\u0154")
        buf.write("\u0155\5\r\7\2\u0155^\3\2\2\2\u0156\u0157\5%\23\2\u0157")
        buf.write("\u0158\5\13\6\2\u0158\u0159\5\3\2\2\u0159\u015a\5\31\r")
        buf.write("\2\u015a`\3\2\2\2\u015b\u015c\5\5\3\2\u015c\u015d\5\37")
        buf.write("\20\2\u015d\u015e\5\37\20\2\u015e\u015f\5\31\r\2\u015f")
        buf.write("\u0160\5\13\6\2\u0160\u0161\5\3\2\2\u0161\u0162\5\35\17")
        buf.write("\2\u0162b\3\2\2\2\u0163\u0164\5\23\n\2\u0164\u0165\5\35")
        buf.write("\17\2\u0165\u0166\5)\25\2\u0166\u0167\5\13\6\2\u0167\u0168")
        buf.write("\5\17\b\2\u0168\u0169\5\13\6\2\u0169\u016a\5%\23\2\u016a")
        buf.write("d\3\2\2\2\u016b\u016c\5\'\24\2\u016c\u016d\5)\25\2\u016d")
        buf.write("\u016e\5%\23\2\u016e\u016f\5\23\n\2\u016f\u0170\5\35\17")
        buf.write("\2\u0170\u0171\5\17\b\2\u0171f\3\2\2\2\u0172\u0173\5\35")
        buf.write("\17\2\u0173\u0174\5\37\20\2\u0174\u0175\5)\25\2\u0175")
        buf.write("h\3\2\2\2\u0176\u0177\5\3\2\2\u0177\u0178\5\35\17\2\u0178")
        buf.write("\u0179\5\t\5\2\u0179j\3\2\2\2\u017a\u017b\5\37\20\2\u017b")
        buf.write("\u017c\5%\23\2\u017cl\3\2\2\2\u017d\u017e\5\t\5\2\u017e")
        buf.write("\u017f\5\23\n\2\u017f\u0180\5-\27\2\u0180n\3\2\2\2\u0181")
        buf.write("\u0182\5\33\16\2\u0182\u0183\5\37\20\2\u0183\u0184\5\t")
        buf.write("\5\2\u0184p\3\2\2\2\u0185\u01a0\5\3\2\2\u0186\u01a0\5")
        buf.write("\5\3\2\u0187\u01a0\5\7\4\2\u0188\u01a0\5\t\5\2\u0189\u01a0")
        buf.write("\5\13\6\2\u018a\u01a0\5\r\7\2\u018b\u01a0\5\17\b\2\u018c")
        buf.write("\u01a0\5\21\t\2\u018d\u01a0\5\23\n\2\u018e\u01a0\5\25")
        buf.write("\13\2\u018f\u01a0\5\27\f\2\u0190\u01a0\5\31\r\2\u0191")
        buf.write("\u01a0\5\33\16\2\u0192\u01a0\5\35\17\2\u0193\u01a0\5\37")
        buf.write("\20\2\u0194\u01a0\5!\21\2\u0195\u01a0\5#\22\2\u0196\u01a0")
        buf.write("\5%\23\2\u0197\u01a0\5\'\24\2\u0198\u01a0\5)\25\2\u0199")
        buf.write("\u01a0\5+\26\2\u019a\u01a0\5-\27\2\u019b\u01a0\5/\30\2")
        buf.write("\u019c\u01a0\5\61\31\2\u019d\u01a0\5\63\32\2\u019e\u01a0")
        buf.write("\5\65\33\2\u019f\u0185\3\2\2\2\u019f\u0186\3\2\2\2\u019f")
        buf.write("\u0187\3\2\2\2\u019f\u0188\3\2\2\2\u019f\u0189\3\2\2\2")
        buf.write("\u019f\u018a\3\2\2\2\u019f\u018b\3\2\2\2\u019f\u018c\3")
        buf.write("\2\2\2\u019f\u018d\3\2\2\2\u019f\u018e\3\2\2\2\u019f\u018f")
        buf.write("\3\2\2\2\u019f\u0190\3\2\2\2\u019f\u0191\3\2\2\2\u019f")
        buf.write("\u0192\3\2\2\2\u019f\u0193\3\2\2\2\u019f\u0194\3\2\2\2")
        buf.write("\u019f\u0195\3\2\2\2\u019f\u0196\3\2\2\2\u019f\u0197\3")
        buf.write("\2\2\2\u019f\u0198\3\2\2\2\u019f\u0199\3\2\2\2\u019f\u019a")
        buf.write("\3\2\2\2\u019f\u019b\3\2\2\2\u019f\u019c\3\2\2\2\u019f")
        buf.write("\u019d\3\2\2\2\u019f\u019e\3\2\2\2\u01a0r\3\2\2\2\u01a1")
        buf.write("\u01a4\5q9\2\u01a2\u01a4\7a\2\2\u01a3\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a9\3\2\2\2\u01a5\u01a8\5q9\2\u01a6")
        buf.write("\u01a8\t\34\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a6\3\2\2")
        buf.write("\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa")
        buf.write("\3\2\2\2\u01aat\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ad")
        buf.write("\7-\2\2\u01adv\3\2\2\2\u01ae\u01af\7,\2\2\u01afx\3\2\2")
        buf.write("\2\u01b0\u01b1\7>\2\2\u01b1\u01b2\7@\2\2\u01b2z\3\2\2")
        buf.write("\2\u01b3\u01b4\7>\2\2\u01b4|\3\2\2\2\u01b5\u01b6\7>\2")
        buf.write("\2\u01b6\u01b7\7?\2\2\u01b7~\3\2\2\2\u01b8\u01b9\7/\2")
        buf.write("\2\u01b9\u0080\3\2\2\2\u01ba\u01bb\7\61\2\2\u01bb\u0082")
        buf.write("\3\2\2\2\u01bc\u01bd\7?\2\2\u01bd\u0084\3\2\2\2\u01be")
        buf.write("\u01bf\7@\2\2\u01bf\u0086\3\2\2\2\u01c0\u01c1\7@\2\2\u01c1")
        buf.write("\u01c2\7?\2\2\u01c2\u0088\3\2\2\2\u01c3\u01c4\t\35\2\2")
        buf.write("\u01c4\u008a\3\2\2\2\u01c5\u01c7\5\u0089E\2\u01c6\u01c5")
        buf.write("\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8")
        buf.write("\u01c9\3\2\2\2\u01c9\u008c\3\2\2\2\u01ca\u01d1\5\u0093")
        buf.write("J\2\u01cb\u01cd\5\u0089E\2\u01cc\u01cb\3\2\2\2\u01cd\u01ce")
        buf.write("\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf")
        buf.write("\u01d1\3\2\2\2\u01d0\u01ca\3\2\2\2\u01d0\u01cc\3\2\2\2")
        buf.write("\u01d1\u01d2\3\2\2\2\u01d2\u01d3\5\u0095K\2\u01d3\u01d6")
        buf.write("\3\2\2\2\u01d4\u01d6\5\u0093J\2\u01d5\u01d0\3\2\2\2\u01d5")
        buf.write("\u01d4\3\2\2\2\u01d6\u008e\3\2\2\2\u01d7\u01da\5W,\2\u01d8")
        buf.write("\u01da\5Y-\2\u01d9\u01d7\3\2\2\2\u01d9\u01d8\3\2\2\2\u01da")
        buf.write("\u0090\3\2\2\2\u01db\u01df\7$\2\2\u01dc\u01de\n\36\2\2")
        buf.write("\u01dd\u01dc\3\2\2\2\u01de\u01e1\3\2\2\2\u01df\u01dd\3")
        buf.write("\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e2\3\2\2\2\u01e1\u01df")
        buf.write("\3\2\2\2\u01e2\u01e3\7$\2\2\u01e3\u01e4\bI\2\2\u01e4\u0092")
        buf.write("\3\2\2\2\u01e5\u01e7\5\u0089E\2\u01e6\u01e5\3\2\2\2\u01e7")
        buf.write("\u01ea\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2")
        buf.write("\u01e9\u01eb\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ed\7")
        buf.write("\60\2\2\u01ec\u01ee\5\u0089E\2\u01ed\u01ec\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2")
        buf.write("\u01f0\u01fe\3\2\2\2\u01f1\u01f3\5\u0089E\2\u01f2\u01f1")
        buf.write("\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4")
        buf.write("\u01f5\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01fa\7\60\2")
        buf.write("\2\u01f7\u01f9\5\u0089E\2\u01f8\u01f7\3\2\2\2\u01f9\u01fc")
        buf.write("\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb")
        buf.write("\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd\u01e8\3\2\2\2")
        buf.write("\u01fd\u01f2\3\2\2\2\u01fe\u0094\3\2\2\2\u01ff\u0201\5")
        buf.write("\13\6\2\u0200\u0202\7/\2\2\u0201\u0200\3\2\2\2\u0201\u0202")
        buf.write("\3\2\2\2\u0202\u0204\3\2\2\2\u0203\u0205\5\u0089E\2\u0204")
        buf.write("\u0203\3\2\2\2\u0205\u0206\3\2\2\2\u0206\u0204\3\2\2\2")
        buf.write("\u0206\u0207\3\2\2\2\u0207\u0096\3\2\2\2\u0208\u0209\7")
        buf.write("*\2\2\u0209\u0098\3\2\2\2\u020a\u020b\7+\2\2\u020b\u009a")
        buf.write("\3\2\2\2\u020c\u020d\7=\2\2\u020d\u009c\3\2\2\2\u020e")
        buf.write("\u020f\7.\2\2\u020f\u009e\3\2\2\2\u0210\u0211\7]\2\2\u0211")
        buf.write("\u00a0\3\2\2\2\u0212\u0213\7_\2\2\u0213\u00a2\3\2\2\2")
        buf.write("\u0214\u0215\7<\2\2\u0215\u00a4\3\2\2\2\u0216\u0217\7")
        buf.write("\60\2\2\u0217\u0218\7\60\2\2\u0218\u00a6\3\2\2\2\u0219")
        buf.write("\u021b\t\37\2\2\u021a\u0219\3\2\2\2\u021b\u021c\3\2\2")
        buf.write("\2\u021c\u021a\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u021e")
        buf.write("\3\2\2\2\u021e\u021f\bT\3\2\u021f\u00a8\3\2\2\2\u0220")
        buf.write("\u0221\7*\2\2\u0221\u0222\7,\2\2\u0222\u0226\3\2\2\2\u0223")
        buf.write("\u0225\13\2\2\2\u0224\u0223\3\2\2\2\u0225\u0228\3\2\2")
        buf.write("\2\u0226\u0227\3\2\2\2\u0226\u0224\3\2\2\2\u0227\u0229")
        buf.write("\3\2\2\2\u0228\u0226\3\2\2\2\u0229\u022a\7,\2\2\u022a")
        buf.write("\u022b\7+\2\2\u022b\u022c\3\2\2\2\u022c\u022d\bU\3\2\u022d")
        buf.write("\u00aa\3\2\2\2\u022e\u0232\7}\2\2\u022f\u0231\13\2\2\2")
        buf.write("\u0230\u022f\3\2\2\2\u0231\u0234\3\2\2\2\u0232\u0233\3")
        buf.write("\2\2\2\u0232\u0230\3\2\2\2\u0233\u0235\3\2\2\2\u0234\u0232")
        buf.write("\3\2\2\2\u0235\u0236\7\177\2\2\u0236\u0237\3\2\2\2\u0237")
        buf.write("\u0238\bV\3\2\u0238\u00ac\3\2\2\2\u0239\u023a\7\61\2\2")
        buf.write("\u023a\u023b\7\61\2\2\u023b\u023f\3\2\2\2\u023c\u023e")
        buf.write("\n \2\2\u023d\u023c\3\2\2\2\u023e\u0241\3\2\2\2\u023f")
        buf.write("\u023d\3\2\2\2\u023f\u0240\3\2\2\2\u0240\u0242\3\2\2\2")
        buf.write("\u0241\u023f\3\2\2\2\u0242\u0243\bW\3\2\u0243\u00ae\3")
        buf.write("\2\2\2\u0244\u0245\13\2\2\2\u0245\u00b0\3\2\2\2\u0246")
        buf.write("\u024a\7$\2\2\u0247\u0249\n!\2\2\u0248\u0247\3\2\2\2\u0249")
        buf.write("\u024c\3\2\2\2\u024a\u0248\3\2\2\2\u024a\u024b\3\2\2\2")
        buf.write("\u024b\u024d\3\2\2\2\u024c\u024a\3\2\2\2\u024d\u024e\b")
        buf.write("Y\4\2\u024e\u00b2\3\2\2\2\31\2\u019f\u01a3\u01a7\u01a9")
        buf.write("\u01c8\u01ce\u01d0\u01d5\u01d9\u01df\u01e8\u01ef\u01f4")
        buf.write("\u01fa\u01fd\u0201\u0206\u021c\u0226\u0232\u023f\u024a")
        buf.write("\5\3I\2\b\2\2\3Y\3")
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
    ID = 30
    ADDOP = 31
    MULOP = 32
    NEQOP = 33
    LTOP = 34
    LTEOP = 35
    SUBOP = 36
    DIVOP = 37
    EQOP = 38
    GTOP = 39
    GTEOP = 40
    INTLIT = 41
    REALIT = 42
    BOOLIT = 43
    STRLIT = 44
    LB = 45
    RB = 46
    SEMI = 47
    COMMA = 48
    LSB = 49
    RSB = 50
    COLON = 51
    DDOT = 52
    WS = 53
    BLOCKCOM_B = 54
    BLOCKCOM_P = 55
    LINECOM = 56
    ERROR_CHAR = 57
    UNCLOSE_STRING = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", "'='", "'>'", 
            "'>='", "'('", "')'", "';'", "','", "'['", "']'", "':'", "'..'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
            "ELSE", "RETURNS", "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
            "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
            "STRING", "NOT", "AND", "OR", "DIV", "MOD", "ID", "ADDOP", "MULOP", 
            "NEQOP", "LTOP", "LTEOP", "SUBOP", "DIVOP", "EQOP", "GTOP", 
            "GTEOP", "INTLIT", "REALIT", "BOOLIT", "STRLIT", "LB", "RB", 
            "SEMI", "COMMA", "LSB", "RSB", "COLON", "DDOT", "WS", "BLOCKCOM_B", 
            "BLOCKCOM_P", "LINECOM", "ERROR_CHAR", "UNCLOSE_STRING" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "BREAK", "CONTINUE", "FOR", "TO", 
                  "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURNS", "WHILE", 
                  "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", 
                  "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "IDCHAR", 
                  "ID", "ADDOP", "MULOP", "NEQOP", "LTOP", "LTEOP", "SUBOP", 
                  "DIVOP", "EQOP", "GTOP", "GTEOP", "DIGIT", "INTLIT", "REALIT", 
                  "BOOLIT", "STRLIT", "NUM_HAS_P", "EXPN", "LB", "RB", "SEMI", 
                  "COMMA", "LSB", "RSB", "COLON", "DDOT", "WS", "BLOCKCOM_B", 
                  "BLOCKCOM_P", "LINECOM", "ERROR_CHAR", "UNCLOSE_STRING" ]

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
            actions[71] = self.STRLIT_action 
            actions[87] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                                        self.text = self.text[1:len(self.text)-1]
                                    
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                            self.text = self.text[1:]    
                            raise UncloseString(self.text)    
                        
     


