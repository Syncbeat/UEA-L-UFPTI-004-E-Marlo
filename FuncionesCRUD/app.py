from flask import Flask, render_template, request, redirect, url_for, make_response
from services.producto_service import ProductoService
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

@app.route('/')
def index():
    productos = ProductoService.listar_todos()
    return render_template('productos/index.html', productos=productos)

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        ProductoService.insertar(nombre, precio, stock)
        return redirect(url_for('index'))
    return render_template('productos/form.html')

@app.route('/eliminar/<int:id>')
def eliminar(id):
    ProductoService.eliminar(id)
    return redirect(url_for('index'))

@app.route('/reporte')
def reporte():
    productos = ProductoService.listar_todos()
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, "Reporte de Inventario - MariaDB")
    
    y = 750
    p.setFont("Helvetica", 12)
    for prod in productos:
        text = f"ID: {prod['id_producto']} | {prod['nombre']} | Precio: ${prod['precio']} | Stock: {prod['stock']}"
        p.drawString(100, y, text)
        y -= 20
        
    p.showPage()
    p.save()
    buffer.seek(0)
    
    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=productos.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)