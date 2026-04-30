async function buscar(){
    var cep = document.getElementById("cep").value;
    cep = cep.replace(/-/g , "");
    if(cep.length != 8){
        document.getElementById("resultado").innerText = "ERRO: CEP Inválido!";
        return;
    }
    for(let i=0; i<cep.length; i++){
        if(isNaN(cep[i])){
            document.getElementById("resultado").innerText = "ERRO: CEP Inválido!";
            return;
        }
    }
    const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
    const data = await response.json();
    if(data.erro){
        document.getElementById("resultado").innerText = "ERRO: CEP não encontrado."
    }
    else{
        var result = 
            `Rua: ${data.logradouro}\n
            Complemento: ${data.complemento}\n
            Bairro: ${data.bairro}\n
            Cidade: ${data.localidade}\n
            Estado: ${data.uf}\n
            `
            document.getElementById("resultado").innerText = result;
    }
}