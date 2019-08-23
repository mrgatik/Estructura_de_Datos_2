using namespace std;

typedef struct nodo{
     int nro;
     struct nodo *izq, *der;
}*ABB;
int numNodos = 0; 
int numK = 0, k;     

ABB crearNodo(int x)
{
     ABB nuevoNodo = new(struct nodo);
     nuevoNodo->nro = x;
     nuevoNodo->izq = NULL;
     nuevoNodo->der = NULL;
     return nuevoNodo;
}

void insertar(ABB &arbol, int x)
{
     if(arbol==NULL)
     {
           arbol = crearNodo(x);
           cout<<"\n\t  Insertado..!"<<endl<<endl;
     }
     else if(x < arbol->nro)
          insertar(arbol->izq, x);
     else if(x > arbol->nro)
          insertar(arbol->der, x);
}

void preOrden(ABB arbol)
{
     if(arbol!=NULL)
     {
          cout << arbol->nro <<" ";
          preOrden(arbol->izq);
          preOrden(arbol->der);
     }
}

void enOrden(ABB arbol)
{
     if(arbol!=NULL)
     {
          enOrden(arbol->izq);
          cout << arbol->nro << " ";
          enOrden(arbol->der);
     }
}

void postOrden(ABB arbol)
{
     if(arbol!=NULL)
     {
          postOrden(arbol->izq);
          postOrden(arbol->der);
          cout << arbol->nro << " ";
     }
}

void verArbol(ABB arbol, int n)
{
     if(arbol==NULL)
          return;
     verArbol(arbol->der, n+1);
     for(int i=0; i<n; i++)
         cout<<"   ";
     numNodos++;
     cout<< arbol->nro <<endl;
     verArbol(arbol->izq, n+1);
}

void menu(string tab)
{
     //system("cls");
     cout << tab;
     cout << "\t1. Crear Arbol (Insertar)\n";
     cout << "\t2. Mostrar Arbol\n";
     cout << "\t3. Recorridos enOrden\n";
     cout << "\t4. Recorridos preOrden\n";
     cout << "\t5. Recorridos postOrden\n";
     cout << "\t6. Salir\n";
     cout << "\n\n\t\t\tSeleccione la opcion que desea: ";
}

int ab(string tab)
{
    ABB arbol = NULL;
    int x;
    int op, op2;
    system("color f9");
    while(true)
    {
          system ("cls");
		  menu(tab);  cin>> op;
          cout << endl;
          switch(op)
          {
            case 1:
            	cout << " Ingrese valor : ";  cin>> x;
            	insertar( arbol, x);
            	cout<<"\n\n\n";
            	system("pause");
                break;
            case 2:
                verArbol(arbol, 0);
                cout<<"\n\n\n";
                system("pause");
                break;
            case 3:
                enOrden(arbol);
                cout<<"\n\n\n";
                system("pause");
                break;
            case 4:
            	  preOrden(arbol); 
            	  cout<<"\n\n\n";
            	  system("pause");
				        break;
			      case 5:
				        postOrden(arbol); 
				        cout<<"\n\n\n";
				        system("pause");
				        break;             
			  default:
				return 0;
				break;
        }
    cout<<"\n\n\n";
    }
}
