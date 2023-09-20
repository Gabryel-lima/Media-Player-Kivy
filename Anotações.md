# Botão com Boxlayout no Kivy

<Tela_inicial>:

    BoxLayout:

    size: root.width, root.height

    BoxLayout:

    orientation: 'vertical'

    size_hint: 0.1, 0.1

    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    Button:

    text: 'Voltar'

    font_size: 30

    size_hint: 0, 1

    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    color: 1,1,1,1

---

# Botão com Gridlayout no Kivy

<Tela_inicial>:
    GridLayout:
        cols: 1  # Uma coluna para o botão
        size: root.width, root.height

    Button:
            text: 'Voltar'
            font_size: 30
            size_hint: 1, None
            height: 100
            color: 1, 1, 1, 1

---

# Botão com Anchorlayout no Kivy

<Tela_inicial>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        size: root.width, root.height

    Button:
            text: 'Voltar'
            font_size: 30
            size_hint: None, None
            size: 100, 50
            color: 1, 1, 1, 1

---

# Usando posicionamento absoluto

<Tela_inicial>:
    Button:
        text: 'Voltar'
        font_size: 30
        size_hint: None, None
        size: 100, 50
        pos: (root.width - self.width) / 2, (root.height - self.height) / 2
        color: 1, 1, 1, 1

---
