"""
Backend Adapter Interface for Triple Lindy

All CAD platform backends should implement this interface.
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional


class BackendAdapter(ABC):
    """Abstract base class for CAD backend adapters."""
    
    @abstractmethod
    def __init__(self, session_config: Optional[Dict[str, Any]] = None) -> None:
        """Initialize the backend with optional configuration."""
        pass
    
    @abstractmethod
    def open_session(self, config: Optional[Dict[str, Any]] = None) -> None:
        """
        Open a session with the CAD software.
        
        Args:
            config: Platform-specific configuration
        """
        pass
    
    @abstractmethod
    def realize(self, csl_ir: Dict[str, Any]) -> Dict[str, str]:
        """
        Execute CSL intermediate representation in the CAD software.
        
        Args:
            csl_ir: CSL intermediate representation
            
        Returns:
            Mapping of CSL feature IDs to platform-specific IDs
        """
        pass
    
    @abstractmethod
    def export(self, export_ops: List[Dict[str, Any]]) -> None:
        """
        Export the current design to various formats.
        
        Args:
            export_ops: List of export operations
        """
        pass
    
    @abstractmethod
    def get_capabilities(self) -> Dict[str, Any]:
        """
        Get the capabilities of this backend.
        
        Returns:
            Dictionary describing supported features, versions, etc.
        """
        pass
    
    @abstractmethod
    def close_session(self) -> None:
        """Close the session with the CAD software."""
        pass
    
    @abstractmethod
    def query_state(self) -> Dict[str, Any]:
        """
        Query the current state of the design.
        
        Returns:
            Dictionary with design information (bodies, sketches, features, etc.)
        """
        pass
