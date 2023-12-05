$(function () {

    $(document).on("click", "#butao", function () {

        var dados_foto = new FormData($('#pow')[0]);

        $.ajax({
            url: 'http://localhost:5000/save_image',
            method: 'POST',
            //dataType: 'json',
            data: dados_foto, // dados serão enviados em formato normal, para upload da foto
            contentType: false,
            cache: false,
            processData: false,
            success: function (data) {
                insertImagemdb();

            },
            error: function (data) {
                alert("deu ruim na foto");
            }
        });





        function insertImagemdb() {

            // só conta a contrabarra uma vez, inicia do zero
            photo = $("#imagem").val().substr(12);

            // preparar dados no formato json
            var dados = JSON.stringify({nome_foto: nome_foto});
            // fazer requisição para o back-end
            $.ajax({
                url: 'http://localhost:5000/incluir_imagem',
                method: 'POST',
                dataType: 'json', // os dados são recebidos no formato json
                //contentType: 'application/json', // dados enviados em json
                data: dados, // estes são os dados enviados
                success: imagem_incluida, // chama a função listar para processar o resultado
                error: erroAoIncluirImagem
            });
            function imagem_incluida(retorno) {
                if (retorno.resultado == "ok") { // a operação deu certo?
                    // informar resultado de sucesso
                    alert("imagem cadastrada com sucesso!");
                } else {
                    // informar mensagem de erro
                    alert(retorno.resultado + ":" + retorno.detalhes);
                }
            }
            function erroAoIncluirImagem(retorno) {
                // informar mensagem de erro
                alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes);
            }
        }

    });
});
