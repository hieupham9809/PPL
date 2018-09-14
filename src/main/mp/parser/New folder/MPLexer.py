# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u029a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\3")
        buf.write("\2\3\2\3\2\3\2\7\2\u00d2\n\2\f\2\16\2\u00d5\13\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\7\3\u00de\n\3\f\3\16\3\u00e1\13")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u00eb\n\4\f\4\16")
        buf.write("\4\u00ee\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5\u010c\n\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3")
        buf.write(",\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3")
        buf.write("@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3")
        buf.write("I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3Q\3")
        buf.write("R\3R\3R\3S\3S\3S\3T\3T\3T\3U\3U\3U\3V\3V\3V\3W\3W\3W\3")
        buf.write("X\3X\3X\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\5Y\u0229\nY\3Z\3Z\3Z\7")
        buf.write("Z\u022e\nZ\fZ\16Z\u0231\13Z\3Z\3Z\3[\3[\3[\3[\5[\u0239")
        buf.write("\n[\3[\3[\3\\\3\\\3\\\3\\\3]\6]\u0242\n]\r]\16]\u0243")
        buf.write("\3]\3]\7]\u0248\n]\f]\16]\u024b\13]\3]\7]\u024e\n]\f]")
        buf.write("\16]\u0251\13]\3]\3]\6]\u0255\n]\r]\16]\u0256\5]\u0259")
        buf.write("\n]\3^\3^\5^\u025d\n^\3^\6^\u0260\n^\r^\16^\u0261\3_\6")
        buf.write("_\u0265\n_\r_\16_\u0266\3`\3`\5`\u026b\n`\3`\6`\u026e")
        buf.write("\n`\r`\16`\u026f\3`\3`\5`\u0274\n`\3a\3a\5a\u0278\na\3")
        buf.write("b\3b\3b\3b\3b\3c\3c\3c\3c\3c\3c\3d\3d\5d\u0287\nd\3d\3")
        buf.write("d\3d\7d\u028c\nd\fd\16d\u028f\13d\3e\6e\u0292\ne\re\16")
        buf.write("e\u0293\3e\3e\3f\3f\3f\4\u00d3\u00df\2g\3\3\5\4\7\5\t")
        buf.write("\2\13\2\r\2\17\6\21\7\23\b\25\t\27\n\31\13\33\f\35\r\37")
        buf.write("\16!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31")
        buf.write("\67\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[")
        buf.write(",]-_.a/c\60e\61g\62i\63k\64m\2o\2q\2s\2u\2w\2y\2{\2}\2")
        buf.write("\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2")
        buf.write("\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099")
        buf.write("\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5\2\u00a7")
        buf.write("\2\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1\2\u00b3\65\u00b5")
        buf.write("\66\u00b7\67\u00b9\2\u00bb\2\u00bd8\u00bf9\u00c1:\u00c3")
        buf.write(";\u00c5<\u00c7=\u00c9>\u00cb?\3\2!\3\2\f\f\3\2\62;\4\2")
        buf.write("CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4")
        buf.write("\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPp")
        buf.write("p\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2")
        buf.write("WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\7\2\f\f")
        buf.write("\17\17$$))^^\t\2$$))ddhhppttvv\5\2\13\f\17\17\"\"\2\u02a8")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2\u00b3\3")
        buf.write("\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00bd\3\2\2\2")
        buf.write("\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5")
        buf.write("\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9\3\2\2\2\2\u00cb\3\2\2")
        buf.write("\2\3\u00cd\3\2\2\2\5\u00db\3\2\2\2\7\u00e6\3\2\2\2\t\u010b")
        buf.write("\3\2\2\2\13\u010d\3\2\2\2\r\u010f\3\2\2\2\17\u0111\3\2")
        buf.write("\2\2\21\u0117\3\2\2\2\23\u0120\3\2\2\2\25\u0124\3\2\2")
        buf.write("\2\27\u012a\3\2\2\2\31\u012d\3\2\2\2\33\u0134\3\2\2\2")
        buf.write("\35\u0139\3\2\2\2\37\u013c\3\2\2\2!\u013f\3\2\2\2#\u0144")
        buf.write("\3\2\2\2%\u0149\3\2\2\2\'\u014d\3\2\2\2)\u0150\3\2\2\2")
        buf.write("+\u0156\3\2\2\2-\u015a\3\2\2\2/\u0161\3\2\2\2\61\u016a")
        buf.write("\3\2\2\2\63\u0174\3\2\2\2\65\u017a\3\2\2\2\67\u017f\3")
        buf.write("\2\2\29\u0187\3\2\2\2;\u018f\3\2\2\2=\u0196\3\2\2\2?\u019a")
        buf.write("\3\2\2\2A\u019e\3\2\2\2C\u01a1\3\2\2\2E\u01a5\3\2\2\2")
        buf.write("G\u01a9\3\2\2\2I\u01ab\3\2\2\2K\u01ad\3\2\2\2M\u01af\3")
        buf.write("\2\2\2O\u01b1\3\2\2\2Q\u01b3\3\2\2\2S\u01b6\3\2\2\2U\u01b8")
        buf.write("\3\2\2\2W\u01ba\3\2\2\2Y\u01bd\3\2\2\2[\u01c0\3\2\2\2")
        buf.write("]\u01c3\3\2\2\2_\u01c5\3\2\2\2a\u01c7\3\2\2\2c\u01c9\3")
        buf.write("\2\2\2e\u01cb\3\2\2\2g\u01cd\3\2\2\2i\u01cf\3\2\2\2k\u01d2")
        buf.write("\3\2\2\2m\u01d4\3\2\2\2o\u01d6\3\2\2\2q\u01d8\3\2\2\2")
        buf.write("s\u01da\3\2\2\2u\u01dc\3\2\2\2w\u01de\3\2\2\2y\u01e0\3")
        buf.write("\2\2\2{\u01e2\3\2\2\2}\u01e4\3\2\2\2\177\u01e6\3\2\2\2")
        buf.write("\u0081\u01e8\3\2\2\2\u0083\u01ea\3\2\2\2\u0085\u01ec\3")
        buf.write("\2\2\2\u0087\u01ee\3\2\2\2\u0089\u01f0\3\2\2\2\u008b\u01f2")
        buf.write("\3\2\2\2\u008d\u01f4\3\2\2\2\u008f\u01f6\3\2\2\2\u0091")
        buf.write("\u01f8\3\2\2\2\u0093\u01fa\3\2\2\2\u0095\u01fc\3\2\2\2")
        buf.write("\u0097\u01fe\3\2\2\2\u0099\u0200\3\2\2\2\u009b\u0202\3")
        buf.write("\2\2\2\u009d\u0204\3\2\2\2\u009f\u0206\3\2\2\2\u00a1\u0208")
        buf.write("\3\2\2\2\u00a3\u020b\3\2\2\2\u00a5\u020e\3\2\2\2\u00a7")
        buf.write("\u0211\3\2\2\2\u00a9\u0214\3\2\2\2\u00ab\u0217\3\2\2\2")
        buf.write("\u00ad\u021a\3\2\2\2\u00af\u021d\3\2\2\2\u00b1\u0228\3")
        buf.write("\2\2\2\u00b3\u022a\3\2\2\2\u00b5\u0234\3\2\2\2\u00b7\u023c")
        buf.write("\3\2\2\2\u00b9\u0258\3\2\2\2\u00bb\u025a\3\2\2\2\u00bd")
        buf.write("\u0264\3\2\2\2\u00bf\u0273\3\2\2\2\u00c1\u0277\3\2\2\2")
        buf.write("\u00c3\u0279\3\2\2\2\u00c5\u027e\3\2\2\2\u00c7\u0286\3")
        buf.write("\2\2\2\u00c9\u0291\3\2\2\2\u00cb\u0297\3\2\2\2\u00cd\u00ce")
        buf.write("\7*\2\2\u00ce\u00cf\7,\2\2\u00cf\u00d3\3\2\2\2\u00d0\u00d2")
        buf.write("\13\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3")
        buf.write("\u00d4\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d6\3\2\2\2")
        buf.write("\u00d5\u00d3\3\2\2\2\u00d6\u00d7\7,\2\2\u00d7\u00d8\7")
        buf.write("+\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\b\2\2\2\u00da\4")
        buf.write("\3\2\2\2\u00db\u00df\7}\2\2\u00dc\u00de\13\2\2\2\u00dd")
        buf.write("\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00df\u00dd\3\2\2\2\u00e0\u00e2\3\2\2\2\u00e1\u00df\3")
        buf.write("\2\2\2\u00e2\u00e3\7\177\2\2\u00e3\u00e4\3\2\2\2\u00e4")
        buf.write("\u00e5\b\3\2\2\u00e5\6\3\2\2\2\u00e6\u00e7\7\61\2\2\u00e7")
        buf.write("\u00e8\7\61\2\2\u00e8\u00ec\3\2\2\2\u00e9\u00eb\n\2\2")
        buf.write("\2\u00ea\u00e9\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea")
        buf.write("\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee")
        buf.write("\u00ec\3\2\2\2\u00ef\u00f0\b\4\2\2\u00f0\b\3\2\2\2\u00f1")
        buf.write("\u010c\5m\67\2\u00f2\u010c\5o8\2\u00f3\u010c\5q9\2\u00f4")
        buf.write("\u010c\5s:\2\u00f5\u010c\5u;\2\u00f6\u010c\5w<\2\u00f7")
        buf.write("\u010c\5y=\2\u00f8\u010c\5{>\2\u00f9\u010c\5}?\2\u00fa")
        buf.write("\u010c\5\177@\2\u00fb\u010c\5\u0081A\2\u00fc\u010c\5\u0083")
        buf.write("B\2\u00fd\u010c\5\u0085C\2\u00fe\u010c\5\u0087D\2\u00ff")
        buf.write("\u010c\5\u0089E\2\u0100\u010c\5\u008bF\2\u0101\u010c\5")
        buf.write("\u008dG\2\u0102\u010c\5\u008fH\2\u0103\u010c\5\u0091I")
        buf.write("\2\u0104\u010c\5\u0093J\2\u0105\u010c\5\u0095K\2\u0106")
        buf.write("\u010c\5\u0097L\2\u0107\u010c\5\u0099M\2\u0108\u010c\5")
        buf.write("\u009bN\2\u0109\u010c\5\u009dO\2\u010a\u010c\5\u009fP")
        buf.write("\2\u010b\u00f1\3\2\2\2\u010b\u00f2\3\2\2\2\u010b\u00f3")
        buf.write("\3\2\2\2\u010b\u00f4\3\2\2\2\u010b\u00f5\3\2\2\2\u010b")
        buf.write("\u00f6\3\2\2\2\u010b\u00f7\3\2\2\2\u010b\u00f8\3\2\2\2")
        buf.write("\u010b\u00f9\3\2\2\2\u010b\u00fa\3\2\2\2\u010b\u00fb\3")
        buf.write("\2\2\2\u010b\u00fc\3\2\2\2\u010b\u00fd\3\2\2\2\u010b\u00fe")
        buf.write("\3\2\2\2\u010b\u00ff\3\2\2\2\u010b\u0100\3\2\2\2\u010b")
        buf.write("\u0101\3\2\2\2\u010b\u0102\3\2\2\2\u010b\u0103\3\2\2\2")
        buf.write("\u010b\u0104\3\2\2\2\u010b\u0105\3\2\2\2\u010b\u0106\3")
        buf.write("\2\2\2\u010b\u0107\3\2\2\2\u010b\u0108\3\2\2\2\u010b\u0109")
        buf.write("\3\2\2\2\u010b\u010a\3\2\2\2\u010c\n\3\2\2\2\u010d\u010e")
        buf.write("\7a\2\2\u010e\f\3\2\2\2\u010f\u0110\t\3\2\2\u0110\16\3")
        buf.write("\2\2\2\u0111\u0112\5o8\2\u0112\u0113\5\u008fH\2\u0113")
        buf.write("\u0114\5u;\2\u0114\u0115\5m\67\2\u0115\u0116\5\u0081A")
        buf.write("\2\u0116\20\3\2\2\2\u0117\u0118\5q9\2\u0118\u0119\5\u0089")
        buf.write("E\2\u0119\u011a\5\u0087D\2\u011a\u011b\5\u0093J\2\u011b")
        buf.write("\u011c\5}?\2\u011c\u011d\5\u0087D\2\u011d\u011e\5\u0095")
        buf.write("K\2\u011e\u011f\5u;\2\u011f\22\3\2\2\2\u0120\u0121\5w")
        buf.write("<\2\u0121\u0122\5\u0089E\2\u0122\u0123\5\u008fH\2\u0123")
        buf.write("\24\3\2\2\2\u0124\u0125\5\u0099M\2\u0125\u0126\5{>\2\u0126")
        buf.write("\u0127\5}?\2\u0127\u0128\5\u0083B\2\u0128\u0129\5u;\2")
        buf.write("\u0129\26\3\2\2\2\u012a\u012b\5\u0093J\2\u012b\u012c\5")
        buf.write("\u0089E\2\u012c\30\3\2\2\2\u012d\u012e\5s:\2\u012e\u012f")
        buf.write("\5\u0089E\2\u012f\u0130\5\u0099M\2\u0130\u0131\5\u0087")
        buf.write("D\2\u0131\u0132\5\u0093J\2\u0132\u0133\5\u0089E\2\u0133")
        buf.write("\32\3\2\2\2\u0134\u0135\5\u0099M\2\u0135\u0136\5}?\2\u0136")
        buf.write("\u0137\5\u0093J\2\u0137\u0138\5{>\2\u0138\34\3\2\2\2\u0139")
        buf.write("\u013a\5s:\2\u013a\u013b\5\u0089E\2\u013b\36\3\2\2\2\u013c")
        buf.write("\u013d\5}?\2\u013d\u013e\5w<\2\u013e \3\2\2\2\u013f\u0140")
        buf.write("\5\u0093J\2\u0140\u0141\5{>\2\u0141\u0142\5u;\2\u0142")
        buf.write("\u0143\5\u0087D\2\u0143\"\3\2\2\2\u0144\u0145\5u;\2\u0145")
        buf.write("\u0146\5\u0083B\2\u0146\u0147\5\u0091I\2\u0147\u0148\5")
        buf.write("u;\2\u0148$\3\2\2\2\u0149\u014a\5\u0097L\2\u014a\u014b")
        buf.write("\5m\67\2\u014b\u014c\5\u008fH\2\u014c&\3\2\2\2\u014d\u014e")
        buf.write("\5\u0089E\2\u014e\u014f\5w<\2\u014f(\3\2\2\2\u0150\u0151")
        buf.write("\5o8\2\u0151\u0152\5u;\2\u0152\u0153\5y=\2\u0153\u0154")
        buf.write("\5}?\2\u0154\u0155\5\u0087D\2\u0155*\3\2\2\2\u0156\u0157")
        buf.write("\5u;\2\u0157\u0158\5\u0087D\2\u0158\u0159\5s:\2\u0159")
        buf.write(",\3\2\2\2\u015a\u015b\5\u008fH\2\u015b\u015c\5u;\2\u015c")
        buf.write("\u015d\5\u0093J\2\u015d\u015e\5\u0095K\2\u015e\u015f\5")
        buf.write("\u008fH\2\u015f\u0160\5\u0087D\2\u0160.\3\2\2\2\u0161")
        buf.write("\u0162\5w<\2\u0162\u0163\5\u0095K\2\u0163\u0164\5\u0087")
        buf.write("D\2\u0164\u0165\5q9\2\u0165\u0166\5\u0093J\2\u0166\u0167")
        buf.write("\5}?\2\u0167\u0168\5\u0089E\2\u0168\u0169\5\u0087D\2\u0169")
        buf.write("\60\3\2\2\2\u016a\u016b\5\u008bF\2\u016b\u016c\5\u008f")
        buf.write("H\2\u016c\u016d\5\u0089E\2\u016d\u016e\5q9\2\u016e\u016f")
        buf.write("\5u;\2\u016f\u0170\5s:\2\u0170\u0171\5\u0095K\2\u0171")
        buf.write("\u0172\5\u008fH\2\u0172\u0173\5u;\2\u0173\62\3\2\2\2\u0174")
        buf.write("\u0175\5m\67\2\u0175\u0176\5\u008fH\2\u0176\u0177\5\u008f")
        buf.write("H\2\u0177\u0178\5m\67\2\u0178\u0179\5\u009dO\2\u0179\64")
        buf.write("\3\2\2\2\u017a\u017b\5\u008fH\2\u017b\u017c\5u;\2\u017c")
        buf.write("\u017d\5m\67\2\u017d\u017e\5\u0083B\2\u017e\66\3\2\2\2")
        buf.write("\u017f\u0180\5o8\2\u0180\u0181\5\u0089E\2\u0181\u0182")
        buf.write("\5\u0089E\2\u0182\u0183\5\u0083B\2\u0183\u0184\5u;\2\u0184")
        buf.write("\u0185\5m\67\2\u0185\u0186\5\u0087D\2\u01868\3\2\2\2\u0187")
        buf.write("\u0188\5}?\2\u0188\u0189\5\u0087D\2\u0189\u018a\5\u0093")
        buf.write("J\2\u018a\u018b\5u;\2\u018b\u018c\5y=\2\u018c\u018d\5")
        buf.write("u;\2\u018d\u018e\5\u008fH\2\u018e:\3\2\2\2\u018f\u0190")
        buf.write("\5\u0091I\2\u0190\u0191\5\u0093J\2\u0191\u0192\5\u008f")
        buf.write("H\2\u0192\u0193\5}?\2\u0193\u0194\5\u0087D\2\u0194\u0195")
        buf.write("\5y=\2\u0195<\3\2\2\2\u0196\u0197\5\u0087D\2\u0197\u0198")
        buf.write("\5\u0089E\2\u0198\u0199\5\u0093J\2\u0199>\3\2\2\2\u019a")
        buf.write("\u019b\5m\67\2\u019b\u019c\5\u0087D\2\u019c\u019d\5s:")
        buf.write("\2\u019d@\3\2\2\2\u019e\u019f\5\u0089E\2\u019f\u01a0\5")
        buf.write("\u008fH\2\u01a0B\3\2\2\2\u01a1\u01a2\5s:\2\u01a2\u01a3")
        buf.write("\5}?\2\u01a3\u01a4\5\u0097L\2\u01a4D\3\2\2\2\u01a5\u01a6")
        buf.write("\5\u0085C\2\u01a6\u01a7\5\u0089E\2\u01a7\u01a8\5s:\2\u01a8")
        buf.write("F\3\2\2\2\u01a9\u01aa\7-\2\2\u01aaH\3\2\2\2\u01ab\u01ac")
        buf.write("\7/\2\2\u01acJ\3\2\2\2\u01ad\u01ae\7,\2\2\u01aeL\3\2\2")
        buf.write("\2\u01af\u01b0\7\61\2\2\u01b0N\3\2\2\2\u01b1\u01b2\7?")
        buf.write("\2\2\u01b2P\3\2\2\2\u01b3\u01b4\7>\2\2\u01b4\u01b5\7@")
        buf.write("\2\2\u01b5R\3\2\2\2\u01b6\u01b7\7>\2\2\u01b7T\3\2\2\2")
        buf.write("\u01b8\u01b9\7@\2\2\u01b9V\3\2\2\2\u01ba\u01bb\7>\2\2")
        buf.write("\u01bb\u01bc\7?\2\2\u01bcX\3\2\2\2\u01bd\u01be\7@\2\2")
        buf.write("\u01be\u01bf\7?\2\2\u01bfZ\3\2\2\2\u01c0\u01c1\7<\2\2")
        buf.write("\u01c1\u01c2\7?\2\2\u01c2\\\3\2\2\2\u01c3\u01c4\7]\2\2")
        buf.write("\u01c4^\3\2\2\2\u01c5\u01c6\7_\2\2\u01c6`\3\2\2\2\u01c7")
        buf.write("\u01c8\7<\2\2\u01c8b\3\2\2\2\u01c9\u01ca\7*\2\2\u01ca")
        buf.write("d\3\2\2\2\u01cb\u01cc\7+\2\2\u01ccf\3\2\2\2\u01cd\u01ce")
        buf.write("\7=\2\2\u01ceh\3\2\2\2\u01cf\u01d0\7\60\2\2\u01d0\u01d1")
        buf.write("\7\60\2\2\u01d1j\3\2\2\2\u01d2\u01d3\7.\2\2\u01d3l\3\2")
        buf.write("\2\2\u01d4\u01d5\t\4\2\2\u01d5n\3\2\2\2\u01d6\u01d7\t")
        buf.write("\5\2\2\u01d7p\3\2\2\2\u01d8\u01d9\t\6\2\2\u01d9r\3\2\2")
        buf.write("\2\u01da\u01db\t\7\2\2\u01dbt\3\2\2\2\u01dc\u01dd\t\b")
        buf.write("\2\2\u01ddv\3\2\2\2\u01de\u01df\t\t\2\2\u01dfx\3\2\2\2")
        buf.write("\u01e0\u01e1\t\n\2\2\u01e1z\3\2\2\2\u01e2\u01e3\t\13\2")
        buf.write("\2\u01e3|\3\2\2\2\u01e4\u01e5\t\f\2\2\u01e5~\3\2\2\2\u01e6")
        buf.write("\u01e7\t\r\2\2\u01e7\u0080\3\2\2\2\u01e8\u01e9\t\16\2")
        buf.write("\2\u01e9\u0082\3\2\2\2\u01ea\u01eb\t\17\2\2\u01eb\u0084")
        buf.write("\3\2\2\2\u01ec\u01ed\t\20\2\2\u01ed\u0086\3\2\2\2\u01ee")
        buf.write("\u01ef\t\21\2\2\u01ef\u0088\3\2\2\2\u01f0\u01f1\t\22\2")
        buf.write("\2\u01f1\u008a\3\2\2\2\u01f2\u01f3\t\23\2\2\u01f3\u008c")
        buf.write("\3\2\2\2\u01f4\u01f5\t\24\2\2\u01f5\u008e\3\2\2\2\u01f6")
        buf.write("\u01f7\t\25\2\2\u01f7\u0090\3\2\2\2\u01f8\u01f9\t\26\2")
        buf.write("\2\u01f9\u0092\3\2\2\2\u01fa\u01fb\t\27\2\2\u01fb\u0094")
        buf.write("\3\2\2\2\u01fc\u01fd\t\30\2\2\u01fd\u0096\3\2\2\2\u01fe")
        buf.write("\u01ff\t\31\2\2\u01ff\u0098\3\2\2\2\u0200\u0201\t\32\2")
        buf.write("\2\u0201\u009a\3\2\2\2\u0202\u0203\t\33\2\2\u0203\u009c")
        buf.write("\3\2\2\2\u0204\u0205\t\34\2\2\u0205\u009e\3\2\2\2\u0206")
        buf.write("\u0207\t\35\2\2\u0207\u00a0\3\2\2\2\u0208\u0209\7^\2\2")
        buf.write("\u0209\u020a\7d\2\2\u020a\u00a2\3\2\2\2\u020b\u020c\7")
        buf.write("^\2\2\u020c\u020d\7h\2\2\u020d\u00a4\3\2\2\2\u020e\u020f")
        buf.write("\7^\2\2\u020f\u0210\7t\2\2\u0210\u00a6\3\2\2\2\u0211\u0212")
        buf.write("\7^\2\2\u0212\u0213\7p\2\2\u0213\u00a8\3\2\2\2\u0214\u0215")
        buf.write("\7^\2\2\u0215\u0216\7v\2\2\u0216\u00aa\3\2\2\2\u0217\u0218")
        buf.write("\7^\2\2\u0218\u0219\7)\2\2\u0219\u00ac\3\2\2\2\u021a\u021b")
        buf.write("\7^\2\2\u021b\u021c\7$\2\2\u021c\u00ae\3\2\2\2\u021d\u021e")
        buf.write("\7^\2\2\u021e\u021f\7^\2\2\u021f\u00b0\3\2\2\2\u0220\u0229")
        buf.write("\5\u00a1Q\2\u0221\u0229\5\u00a3R\2\u0222\u0229\5\u00a5")
        buf.write("S\2\u0223\u0229\5\u00a7T\2\u0224\u0229\5\u00a9U\2\u0225")
        buf.write("\u0229\5\u00abV\2\u0226\u0229\5\u00adW\2\u0227\u0229\5")
        buf.write("\u00afX\2\u0228\u0220\3\2\2\2\u0228\u0221\3\2\2\2\u0228")
        buf.write("\u0222\3\2\2\2\u0228\u0223\3\2\2\2\u0228\u0224\3\2\2\2")
        buf.write("\u0228\u0225\3\2\2\2\u0228\u0226\3\2\2\2\u0228\u0227\3")
        buf.write("\2\2\2\u0229\u00b2\3\2\2\2\u022a\u022f\7$\2\2\u022b\u022e")
        buf.write("\n\36\2\2\u022c\u022e\5\u00b1Y\2\u022d\u022b\3\2\2\2\u022d")
        buf.write("\u022c\3\2\2\2\u022e\u0231\3\2\2\2\u022f\u022d\3\2\2\2")
        buf.write("\u022f\u0230\3\2\2\2\u0230\u0232\3\2\2\2\u0231\u022f\3")
        buf.write("\2\2\2\u0232\u0233\bZ\3\2\u0233\u00b4\3\2\2\2\u0234\u0238")
        buf.write("\5\u00b3Z\2\u0235\u0236\7^\2\2\u0236\u0239\n\37\2\2\u0237")
        buf.write("\u0239\7)\2\2\u0238\u0235\3\2\2\2\u0238\u0237\3\2\2\2")
        buf.write("\u0239\u023a\3\2\2\2\u023a\u023b\b[\4\2\u023b\u00b6\3")
        buf.write("\2\2\2\u023c\u023d\5\u00b3Z\2\u023d\u023e\7$\2\2\u023e")
        buf.write("\u023f\b\\\5\2\u023f\u00b8\3\2\2\2\u0240\u0242\5\r\7\2")
        buf.write("\u0241\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0241\3")
        buf.write("\2\2\2\u0243\u0244\3\2\2\2\u0244\u0245\3\2\2\2\u0245\u0249")
        buf.write("\7\60\2\2\u0246\u0248\5\r\7\2\u0247\u0246\3\2\2\2\u0248")
        buf.write("\u024b\3\2\2\2\u0249\u0247\3\2\2\2\u0249\u024a\3\2\2\2")
        buf.write("\u024a\u0259\3\2\2\2\u024b\u0249\3\2\2\2\u024c\u024e\5")
        buf.write("\r\7\2\u024d\u024c\3\2\2\2\u024e\u0251\3\2\2\2\u024f\u024d")
        buf.write("\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u0252\3\2\2\2\u0251")
        buf.write("\u024f\3\2\2\2\u0252\u0254\7\60\2\2\u0253\u0255\5\r\7")
        buf.write("\2\u0254\u0253\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u0254")
        buf.write("\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0259\3\2\2\2\u0258")
        buf.write("\u0241\3\2\2\2\u0258\u024f\3\2\2\2\u0259\u00ba\3\2\2\2")
        buf.write("\u025a\u025c\t\b\2\2\u025b\u025d\7/\2\2\u025c\u025b\3")
        buf.write("\2\2\2\u025c\u025d\3\2\2\2\u025d\u025f\3\2\2\2\u025e\u0260")
        buf.write("\5\r\7\2\u025f\u025e\3\2\2\2\u0260\u0261\3\2\2\2\u0261")
        buf.write("\u025f\3\2\2\2\u0261\u0262\3\2\2\2\u0262\u00bc\3\2\2\2")
        buf.write("\u0263\u0265\5\r\7\2\u0264\u0263\3\2\2\2\u0265\u0266\3")
        buf.write("\2\2\2\u0266\u0264\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u00be")
        buf.write("\3\2\2\2\u0268\u026a\5\u00b9]\2\u0269\u026b\5\u00bb^\2")
        buf.write("\u026a\u0269\3\2\2\2\u026a\u026b\3\2\2\2\u026b\u0274\3")
        buf.write("\2\2\2\u026c\u026e\5\r\7\2\u026d\u026c\3\2\2\2\u026e\u026f")
        buf.write("\3\2\2\2\u026f\u026d\3\2\2\2\u026f\u0270\3\2\2\2\u0270")
        buf.write("\u0271\3\2\2\2\u0271\u0272\5\u00bb^\2\u0272\u0274\3\2")
        buf.write("\2\2\u0273\u0268\3\2\2\2\u0273\u026d\3\2\2\2\u0274\u00c0")
        buf.write("\3\2\2\2\u0275\u0278\5\u00c3b\2\u0276\u0278\5\u00c5c\2")
        buf.write("\u0277\u0275\3\2\2\2\u0277\u0276\3\2\2\2\u0278\u00c2\3")
        buf.write("\2\2\2\u0279\u027a\5\u0093J\2\u027a\u027b\5\u008fH\2\u027b")
        buf.write("\u027c\5\u0095K\2\u027c\u027d\5u;\2\u027d\u00c4\3\2\2")
        buf.write("\2\u027e\u027f\5w<\2\u027f\u0280\5m\67\2\u0280\u0281\5")
        buf.write("\u0083B\2\u0281\u0282\5\u0091I\2\u0282\u0283\5u;\2\u0283")
        buf.write("\u00c6\3\2\2\2\u0284\u0287\5\t\5\2\u0285\u0287\5\13\6")
        buf.write("\2\u0286\u0284\3\2\2\2\u0286\u0285\3\2\2\2\u0287\u028d")
        buf.write("\3\2\2\2\u0288\u028c\5\t\5\2\u0289\u028c\5\13\6\2\u028a")
        buf.write("\u028c\5\r\7\2\u028b\u0288\3\2\2\2\u028b\u0289\3\2\2\2")
        buf.write("\u028b\u028a\3\2\2\2\u028c\u028f\3\2\2\2\u028d\u028b\3")
        buf.write("\2\2\2\u028d\u028e\3\2\2\2\u028e\u00c8\3\2\2\2\u028f\u028d")
        buf.write("\3\2\2\2\u0290\u0292\t \2\2\u0291\u0290\3\2\2\2\u0292")
        buf.write("\u0293\3\2\2\2\u0293\u0291\3\2\2\2\u0293\u0294\3\2\2\2")
        buf.write("\u0294\u0295\3\2\2\2\u0295\u0296\be\2\2\u0296\u00ca\3")
        buf.write("\2\2\2\u0297\u0298\13\2\2\2\u0298\u0299\bf\6\2\u0299\u00cc")
        buf.write("\3\2\2\2\33\2\u00d3\u00df\u00ec\u010b\u0228\u022d\u022f")
        buf.write("\u0238\u0243\u0249\u024f\u0256\u0258\u025c\u0261\u0266")
        buf.write("\u026a\u026f\u0273\u0277\u0286\u028b\u028d\u0293\7\b\2")
        buf.write("\2\3Z\2\3[\3\3\\\4\3f\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT1 = 1
    COMMENT2 = 2
    COMMENT3 = 3
    BREAK = 4
    CONTINUE = 5
    FOR = 6
    WHILE = 7
    TO = 8
    DOWNTO = 9
    WITH = 10
    DO = 11
    IF = 12
    THEN = 13
    ELSE = 14
    VAR = 15
    OF = 16
    BEGIN = 17
    END = 18
    RETURN = 19
    FUNCTION = 20
    PROCEDURE = 21
    ARRAY = 22
    REAL = 23
    BOOLEAN = 24
    INTEGER = 25
    STRING = 26
    NOT = 27
    AND = 28
    OR = 29
    DIV = 30
    MOD = 31
    ADD = 32
    SUB = 33
    MUL = 34
    DIV_F = 35
    EQ = 36
    NEQ = 37
    LESSTHAN = 38
    GREATERTHAN = 39
    LESSEQ = 40
    GREATEREQ = 41
    ASSIGN = 42
    LSB = 43
    RSB = 44
    CL = 45
    LB = 46
    RB = 47
    SM = 48
    DDOT = 49
    CM = 50
    UNCLOSE_STRING = 51
    ILLEGAL_ESCAPE = 52
    STRINGLIT = 53
    INTLIT = 54
    REALLIT = 55
    BOOLEANLIT = 56
    TRUE = 57
    FALSE = 58
    ID = 59
    WS = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'='", "'<>'", "'<'", "'>'", "'<='", 
            "'>='", "':='", "'['", "']'", "':'", "'('", "')'", "';'", "'..'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT1", "COMMENT2", "COMMENT3", "BREAK", "CONTINUE", "FOR", 
            "WHILE", "TO", "DOWNTO", "WITH", "DO", "IF", "THEN", "ELSE", 
            "VAR", "OF", "BEGIN", "END", "RETURN", "FUNCTION", "PROCEDURE", 
            "ARRAY", "REAL", "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", 
            "OR", "DIV", "MOD", "ADD", "SUB", "MUL", "DIV_F", "EQ", "NEQ", 
            "LESSTHAN", "GREATERTHAN", "LESSEQ", "GREATEREQ", "ASSIGN", 
            "LSB", "RSB", "CL", "LB", "RB", "SM", "DDOT", "CM", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "STRINGLIT", "INTLIT", "REALLIT", "BOOLEANLIT", 
            "TRUE", "FALSE", "ID", "WS", "ERROR_CHAR" ]

    ruleNames = [ "COMMENT1", "COMMENT2", "COMMENT3", "LETTER", "UNDERSCORE", 
                  "DIGIT", "BREAK", "CONTINUE", "FOR", "WHILE", "TO", "DOWNTO", 
                  "WITH", "DO", "IF", "THEN", "ELSE", "VAR", "OF", "BEGIN", 
                  "END", "RETURN", "FUNCTION", "PROCEDURE", "ARRAY", "REAL", 
                  "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", "OR", "DIV", 
                  "MOD", "ADD", "SUB", "MUL", "DIV_F", "EQ", "NEQ", "LESSTHAN", 
                  "GREATERTHAN", "LESSEQ", "GREATEREQ", "ASSIGN", "LSB", 
                  "RSB", "CL", "LB", "RB", "SM", "DDOT", "CM", "A", "B", 
                  "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", 
                  "Y", "Z", "BSP", "FF", "CR", "NL", "TAB", "SQ", "DQ", 
                  "BSL", "LEGAL_ESCAPE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STRINGLIT", "Decimal_point", "Scientific_notation", "INTLIT", 
                  "REALLIT", "BOOLEANLIT", "TRUE", "FALSE", "ID", "WS", 
                  "ERROR_CHAR" ]

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
            actions[88] = self.UNCLOSE_STRING_action 
            actions[89] = self.ILLEGAL_ESCAPE_action 
            actions[90] = self.STRINGLIT_action 
            actions[100] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

               		raise UncloseString(self.text[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:


             	   raise IllegalEscape(self.text[1:])
            	
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                	self.text = self.text[1:-1]
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

              		 raise ErrorToken(self.text)
            	
     


