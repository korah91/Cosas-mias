/**
 * Ejemplo Hooks:
 * - useState()
 * - useContext()
 */

import React, {useState, useContext} from 'react';

/**
 * 
 * @returns Componente1
 * Dispone de un contexto que va a tener un valor 
 * que recibe el padre
 */
const Componente1 = () => {
    // Inicializamos un estado vacio que se rellenara
    // con los datos del padre
    const state = React.createContext(null);

    return (
        <div>
            <h1>
                El Token es: {state.token}
            </h1>
            <Componente2></Componente2>
        </div>
    );
}

const Componente2 = () => {
    const state = useContext(miContexto);


    return (
        <div>
            <h2>
                La sesión es: {state.sesion}
            </h2>        
        </div>
    );
}

export default function MiComponenteConContexto() {
  return (

    const estadoInicial

    <div>Ejemplo3</div>
  )
}

