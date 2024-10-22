import streamlit as st

# Função refatorada para criar cadastros no Streamlit
def pxtelacria_streamlit():
    st.title('Cadastro de Itens')
    
    # Inputs para cadastro
    item_name = st.text_input('Nome do Item:')
    item_code = st.text_input('Código do Item:')
    item_quantity = st.number_input('Quantidade:', min_value=0, step=1)
    item_price = st.number_input('Preço (R$):', min_value=0.0, format="%.2f")

    # Botão para salvar as informações do item
    if st.button('Salvar'):
        if item_name and item_code:
            # Exibe as informações cadastradas
            st.success(f'Item "{item_name}" cadastrado com sucesso!')
            st.write(f'Código: {item_code}')
            st.write(f'Quantidade: {item_quantity}')
            st.write(f'Preço: R$ {item_price:.2f}')
        else:
            st.error('Por favor, preencha o nome e o código do item.')

# Rodar a função de cadastro no Streamlit
if __name__ == "__main__":
    pxtelacria_streamlit()
