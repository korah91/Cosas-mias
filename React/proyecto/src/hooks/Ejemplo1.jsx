/**
 * Ejemplo de uso del Hook useState
 * 
 * Crear un componente de tipo función y acceder a su estado
 * privado a través de un hook y además poder modificarlo
 */

import React, { useState } from 'react';

const Ejemplo1 = () => {

    // Valor inicial para un contador
    const valorInicial = 0;
    
    // Valor inicial para una persona
    const personaInicial = {
        nombre: 'Martin',
        email: 'martin@imagina.com'
    }

    /**
     * Queremos que el valorInicial y personaInicial sean parte
     * del estado del componente para asi poder gestionar su cambio
     * y que este se vea reflejado en la vista del componente
     * 
     * const [nombreVariable, funcionParaCambiar] = useState(valorInicial)
     */
    const [contador, setContador] = useState(valorInicial);
    const [persona, setPersona] = useState(personaInicial)

    /**
     * Funcion para actualizar el estado privado que contiene el contador
     */
    function incrementarContador(){
        // ? funcionParaCambiar(nuevoValor)
        setContador(contador + 1);
    }


    /**
     * Funcion para actualizar el estado de persona en el componente
     */
    function actualizarPersona(){
        setPersona({
            nombre: 'Pepe',
            email: 'pepe@gmail.com'
        })

    }

    return (
        <div>
            <h1>Ejemplo de useState</h1>
            <h2>Contador: {contador}</h2>
            <h2>Persona:</h2>
            <h3>Nombre: {persona.nombre}</h3>
            <h3>email: {persona.email}</h3>
            <button onClick={incrementarContador}>contador</button>
            <button onClick={actualizarPersona}>persona</button>
        </div>
    );
}

export default Ejemplo1;
