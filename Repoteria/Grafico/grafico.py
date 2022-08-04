class GeneraGrafico:
  def grafico(self):

    import matplotlib.pyplot as plt
    import numpy as np

    import mysql.connector

    mydb = mysql.connector.connect(
      host='192.168.0.115',
      user='victor',
      password='192.168.1.2',
      database='test')

    mycursor = mydb.cursor()

    mycursor.execute("select hombres, mujeres, grupo from puntuacion")

    myresult = mycursor.fetchall()

    h = []
    m = []
    g = []

    for i in myresult:
      h.append(i[0])
      m.append(i[1])
      g.append(i[2])

    labels = g
    men_means = h
    women_means = m

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Hombre')
    rects2 = ax.bar(x + width/2, women_means, width, label='Mujer')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Puntuaciones')
    ax.set_title('Puntuaciones por grupo y género')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    fig.savefig("Informe/test.png")
    plt.show()
