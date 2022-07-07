from PyQt5 import QtCore, QtWidgets, QtSql
import sys


def addRecord():
    stm.insertRow(stm.rowCount())


def delRecord():
    stm.removeRow(tv.currentIndex().row())
    stm.select()


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QRelationalSqlTableModel")
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()

stm = QtSql.QSqlRelationalTableModel(parent=window)
stm.setTable('good')
stm.setSort(1, QtCore.Qt.AscendingOrder)
stm.setRelation(3, QtSql.QSqlRelation('category', 'id', 'catname'))
stm.select()

stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Quantity')
stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Category')

vbox = QtWidgets.QVBoxLayout()
tv = QtWidgets.QTableView()
tv.setModel(stm)
tv.setItemDelegateForColumn(3, QtSql.QSqlRelationalDelegate(tv))
tv.hideColumn(0)
tv.setColumnWidth(1, 150)
tv.setColumnWidth(2, 60)
tv.setColumnWidth(3, 150)
vbox.addWidget(tv)

btnAdd = QtWidgets.QPushButton("&Add record")
btnAdd.clicked.connect(addRecord)
vbox.addWidget(btnAdd)

btnDel = QtWidgets.QPushButton("&Delete record")
btnDel.clicked.connect(delRecord)
vbox.addWidget(btnDel)

window.setLayout(vbox)
window.resize(450, 450)
window.show()
sys.exit(app.exec_())

# window = QtWidgets.QTableView()
# window.setWindowTitle("QSqlQueryModel")
# con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
# con.setDatabaseName('data.sqlite')
# con.open()
# sqm = QtSql.QSqlQueryModel(parent=window)
# sqm.setQuery('select * from good order by goodname')
#
# sqm.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
# sqm.setHeaderData(2, QtCore.Qt.Horizontal, 'Quantity')
# window.setModel(sqm)
# window.hideColumn(0)
# window.setColumnWidth(1, 230)
# window.setColumnWidth(2, 230)
# window.resize(500, 250)
# window.show()
# sys.exit(app.exec_())
# query = QtSql.QSqlQuery()
# query.exec("select * from good order by goodcount")
# lst = []
# if query.isActive():
#     query.first()
#     while query.isValid():
#         lst.append(query.value('goodname') + ': ' +
#                    str(query.value('goodcount')) + 'шт.')
#         print(lst[len(lst) - 1])
#         query.next()
# if 'good' not in con.tables():
#     query = QtSql.QSqlQuery()
#     query.exec("create table good(id integer primary key autoincrement,"
#                "goodname text, goodcount integer) ")
# query = QtSql.QSqlQuery()
# query.prepare('insert into good values(null, :name, :count)')
# list1 = ['Paper', 'Photopaper', 'Catridge']
# list2 = [15, 8, 3]
# query.bindValue(':name', list1)
# query.bindValue(':count', list2)
# query.execBatch()
# con.close()
