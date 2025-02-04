// Aguarda o carregamento completo do conteúdo da página
document.addEventListener('DOMContentLoaded', function() {
    // Seleção dos elementos no DOM
    const lista = document.getElementById('lista'); // Onde os posts serão exibidos
    const modal = document.getElementById('modal'); // Modal onde os comentários serão exibidos
    const info = document.getElementById('info'); // Elemento dentro do modal que conterá os comentários
    const fechar = modal.querySelector('.close-btn'); // Botão para fechar o modal

    // Função assíncrona para carregar os posts e usuários
    async function carregar() {
        try {
            // Carrega os posts via API
            let resPosts = await fetch('https://jsonplaceholder.typicode.com/posts');
            let posts = await resPosts.json(); // Converte a resposta em JSON

            // Carrega os usuários via API
            let resUsers = await fetch('https://jsonplaceholder.typicode.com/users');
            let usuarios = await resUsers.json(); // Converte a resposta em JSON
            
            lista.innerHTML = ''; // Limpa a lista antes de adicionar novos posts

            // Laço para exibir os primeiros 10 posts
            for (let i = 0; i < 10; i++) {
                if (posts[i]) {
                    // Encontra o usuário associado ao post
                    let usuario = usuarios.find(u => u.id === posts[i].userId);
                    // Chama a função criar para gerar o HTML dos posts
                    criar(posts[i], usuario);
                }
            }
        } catch (erro) {
            // Exibe erro caso ocorra falha ao carregar os dados
            lista.innerHTML = `<div class="alert error">Erro ao carregar: ${erro.message}</div>`;
        }
    }
    
    // Chama a função para carregar os dados quando a página carrega
    carregar();
    
    // Função que cria e exibe cada post na lista
    function criar(post, usuario) {
        if (post.title && post.body && usuario) {
            // Cria o HTML de cada post com os detalhes
            let itemHtml = `
                <article class="item">
                    <div class="topo">
                        <div class="info">
                            <h5>${post.title}</h5> <!-- Título do post -->
                            <p>${post.body}</p> <!-- Corpo do post -->
                            <small><strong>${usuario.username}</strong> - ${usuario.email}</small> <!-- Informações do usuário -->
                        </div>
                        <div class="acoes">
                            <button class="btn" onclick="detalhes(${post.id})"> <!-- Botão para abrir comentários -->
                                <span>Comentários</span>
                            </button>
                        </div>
                    </div>
                </article>
            `;
            lista.innerHTML += itemHtml; // Adiciona o HTML gerado ao conteúdo da lista
        }
    }

    // Função chamada quando o botão de "Comentários" é clicado
    window.detalhes = async function(id) {
        try {
            // Exibe o indicador de carregamento enquanto busca os comentários
            info.innerHTML = '<div class="text-center"><div class="spinner"></div></div>';
            
            // Carrega os comentários do post
            let res = await fetch(`https://jsonplaceholder.typicode.com/comments?postId=${id}`);
            let comentarios = await res.json(); // Converte a resposta em JSON
            
            let infoHtml = '';
            // Loop para exibir os comentários
            for (let comentario of comentarios) {
                infoHtml += `
                    <div class="coment">
                        <h6>${comentario.name}</h6> <!-- Nome do comentário -->
                        <p><strong>Email:</strong> ${comentario.email}</p> <!-- E-mail do comentarista -->
                        <p>${comentario.body}</p> <!-- Corpo do comentário -->
                    </div>
                `;
            }

            // Exibe os comentários ou uma mensagem de aviso caso não haja comentários
            info.innerHTML = infoHtml || '<div class="alert warning">Nenhum comentário encontrado.</div>';
            // Exibe o modal
            modal.classList.add('show');
            modal.style.display = 'block';
        } catch (erro) {
            // Exibe erro se não conseguir carregar os comentários
            info.innerHTML = `<div class="alert error">Erro ao carregar: ${erro.message}</div>`;
        }
    }

    // Fecha o modal quando o botão de fechar é clicado
    fechar.addEventListener('click', function() {
        modal.classList.remove('show');
        modal.style.display = 'none';
    });
});
