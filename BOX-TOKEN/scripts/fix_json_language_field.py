#!/usr/bin/env python3
"""
Script para corrigir arquivo JSON adicionando o campo "language": "Solidity"
específico para BOX Token - NÃO mexe em arquivos do NEOFLW
"""
import json
import sys
from pathlib import Path

def fix_json_language_field(input_file: str, output_file: str = None):
    """
    Adiciona o campo "language": "Solidity" ao JSON se estiver faltando
    
    Args:
        input_file: Caminho para o arquivo JSON de entrada
        output_file: Caminho para o arquivo JSON de saída (opcional)
    """
    input_path = Path(input_file)
    
    if not input_path.exists():
        print(f"❌ Arquivo não encontrado: {input_file}")
        return False
    
    print(f"📂 Lendo: {input_path}")
    
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Erro ao ler JSON: {e}")
        return False
    
    # Verifica se já tem o campo language
    if "language" in data:
        print("✅ Campo 'language' já existe no JSON")
        print(f"   Valor atual: {data['language']}")
        
        if data["language"] != "Solidity":
            response = input("   O valor não é 'Solidity'. Deseja corrigir? (s/n): ")
            if response.lower() == 's':
                data["language"] = "Solidity"
                print("   ✅ Campo 'language' atualizado para 'Solidity'")
            else:
                print("   ⚠️  Mantendo valor original")
        else:
            print("   ✅ Campo 'language' já está correto ('Solidity')")
            return True
    else:
        # Adiciona o campo language
        print("⚠️  Campo 'language' não encontrado. Adicionando...")
        
        # Cria um novo dicionário com language primeiro
        new_data = {"language": "Solidity"}
        new_data.update(data)
        data = new_data
        
        print("   ✅ Campo 'language': 'Solidity' adicionado")
    
    # Define arquivo de saída
    if output_file:
        output_path = Path(output_file)
    else:
        # Cria arquivo com sufixo _fixed
        output_path = input_path.parent / f"{input_path.stem}_fixed.json"
    
    # Salva o JSON corrigido
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ JSON corrigido salvo em: {output_path}")
        print(f"   Tamanho: {output_path.stat().st_size} bytes")
        
        # Verifica se tem os campos essenciais
        required_fields = ["language", "sources", "settings"]
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            print(f"\n⚠️  ATENÇÃO: Campos faltando: {', '.join(missing_fields)}")
            print("   O JSON pode precisar de mais ajustes.")
        else:
            print("\n✅ Todos os campos essenciais estão presentes!")
            print("   - language: ✅")
            print("   - sources: ✅")
            print("   - settings: ✅")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao salvar arquivo: {e}")
        return False

def main():
    """Função principal"""
    print("🔧 Corrigir JSON - Adicionar Campo 'language'\n")
    print("⚠️  Este script é APENAS para arquivos do BOX Token\n")
    
    if len(sys.argv) < 2:
        print("Uso: python fix_json_language_field.py <arquivo_json> [arquivo_saida]")
        print("\nExemplo:")
        print("  python fix_json_language_field.py box_token.json")
        print("  python fix_json_language_field.py box_token.json box_token_fixed.json")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = fix_json_language_field(input_file, output_file)
    
    if success:
        print("\n✅ Pronto! Você pode usar o arquivo corrigido no BSCScan.")
        print("   Cole o conteúdo do arquivo no campo 'Standard JSON Input'")
    else:
        print("\n❌ Falha ao corrigir o JSON. Verifique o arquivo e tente novamente.")
        sys.exit(1)

if __name__ == "__main__":
    main()

